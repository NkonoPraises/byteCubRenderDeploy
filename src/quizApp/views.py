

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, QuizSubmission, Answer, LeaderboardEntry,ImageUpload
from django.db.models import Sum, F
from django.db import transaction

def base_view(request):
    return render(request, 'base.html')

@login_required(login_url="login")
def quiz_page(request, quiz_name):
    quizzes = Quiz.objects.filter(quiz_name=quiz_name)
    if not quizzes:
        return HttpResponse("No quizzes with this name found.")
    return render(request, 'quizApp/quiz_page.html', {'quizzes': quizzes})

@login_required(login_url="login")
def submit_quiz(request, quiz_name):
    if request.method == 'POST':
        quizzes = Quiz.objects.filter(quiz_name=quiz_name)
        if not quizzes:
            return HttpResponse("No quizzes with this name found.")

        total_score = 0
        answers_data = []

        for quiz in quizzes:
            print(f" Quiz one is: {quiz}")
            
            # Check if user already submitted this quiz and delete it
            existing_submission = QuizSubmission.objects.filter(
                user=request.user, 
                quiz=quiz
            ).first()
            
            if existing_submission:
                # Delete the entire existing submission (including answers via cascade)
                existing_submission.delete()
            
            # Create new submission
            submission = QuizSubmission.objects.create(user=request.user, quiz=quiz)
            quiz_score = 0

            for question in quiz.questions.all():
                chosen_answer = request.POST.get(f'question_{question.id}')
                is_correct = (chosen_answer == question.correct_answer)

                Answer.objects.create(submission=submission, question=question, chosen_answer=chosen_answer)

                if is_correct:
                    quiz_score += 1

            submission.score = quiz_score
            submission.save()

            total_score += quiz_score

            answers_data.append({
                'quiz': quiz,
                'submission': submission,
                'answers': submission.answers.all(),
            })

        update_leaderboard(request.user, total_score)  # Call the leaderboard update function
        return redirect('quizApp:answer_page', quiz_name=quiz_name)
    else:
        return HttpResponse("Invalid request method.")

@login_required(login_url="login")
def answer_page(request, quiz_name):
    quizzes = Quiz.objects.filter(quiz_name=quiz_name)
    if not quizzes:
        return HttpResponse("No quizzes with this name found.")

    recent_submission = QuizSubmission.objects.filter(user=request.user, quiz__in=quizzes).latest('submission_time')

    answers_data = []
    for quiz in quizzes:
        print(f" Quiz two is: {quiz}")
        try:
            submission = QuizSubmission.objects.get(user=request.user, quiz=quiz)
            answers = submission.answers.all()
            answers_data.append({
                'quiz': quiz,
                'submission': submission,
                'answers': submission.answers.all(),
            })
        except QuizSubmission.DoesNotExist:
            answers_data.append({
                'quiz': quiz,
                'submission': None,
                'answers': None,
            })

    recent_score = recent_submission.score
    total_score = QuizSubmission.objects.filter(user=request.user).aggregate(Sum('score'))['score__sum'] or 0
    leaderboard = LeaderboardEntry.objects.order_by('-total_score')
    # rank = LeaderboardEntry.objects.filter(total_score__gt=LeaderboardEntry.objects.get(user=request.user).total_score).count() + 1
    # Get the current user's LeaderboardEntry
    current_entry = LeaderboardEntry.objects.get(user=request.user)

    # Calculate the rank by counting users in the same level with a higher score
    rank = LeaderboardEntry.objects.filter(
        ranking_score=current_entry.ranking_score,  # Same level
        total_score__gt=current_entry.total_score   # Higher score
    ).count() + 1

    return render(request, 'quizApp/answer_page.html', {
        'quiz':quiz,
        'answers_data': answers_data,
        'recent_score': recent_score,
        'total_score': total_score,
        'leaderboard': leaderboard,
        'rank': rank,
        'quiz_name': quiz_name,
    })

@transaction.atomic
def update_leaderboard(user, score):
    try:
        leaderboard_entry = LeaderboardEntry.objects.get(user=user)
        leaderboard_entry.total_score = F('total_score') + score
        leaderboard_entry.save()
    except LeaderboardEntry.DoesNotExist:
        LeaderboardEntry.objects.create(user=user, total_score=score)


def upload_image(request):
    images = ImageUpload.objects.all()
    return render(request, 'quizApp/upload_image.html', {'images': images})