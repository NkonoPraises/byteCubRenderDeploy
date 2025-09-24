from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Exercise, CodeSubmission
from .forms import CodeSubmissionForm
from difflib import SequenceMatcher
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Exercise, CodeSubmission
from .forms import CodeSubmissionForm
from .utils import compare_code  # Import the compare_code function
from django.http import HttpResponse,Http404
from quizApp.models import *
from django.contrib import messages

# @login_required(login_url="login")
# def exercise_list(request):
#     exercises = Exercise.objects.all()
#     print(f'Exercises are {exercises}')
#     return render(request, 'exercise_list.html', {'exercises': exercises})

# def test(request):
#     return HttpResponse("Hello world")



# @login_required(login_url="login")
# def exercise_detail(request, exercise_id):
#     exercise = get_object_or_404(Exercise, pk=exercise_id)

#     if request.method == 'POST':
#         form = CodeSubmissionForm(request.POST)
#         if form.is_valid():
#             submission = form.save(commit=False)
#             submission.user = request.user
#             submission.exercise = exercise
#             submission.save()

#             # Compare code using the imported function
#             comparison_result = compare_code(submission.code, exercise.reference_code)
#             submission.score = comparison_result['score']  # Access the score from the dict
#             submission.save()

#             return redirect('exerciseApp:submission_detail', submission_id=submission.id)
#     else:
#         form = CodeSubmissionForm()

#     return render(request, 'exercise_detail.html', {'exercise': exercise, 'form': form})

# @login_required(login_url="login")
# def submission_detail(request, submission_id):
#     submission = get_object_or_404(CodeSubmission, pk=submission_id, user=request.user)
#     return render(request, 'submission_detail.html', {'submission': submission})



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Exercise, CodeSubmission, CompletedExercise
from .forms import CodeSubmissionForm
from .utils import compare_code  # Import the compare_code function
from django.urls import reverse
from django.db.models import F

@login_required(login_url="login")
def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercise_list.html', {'exercises': exercises})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Exercise, CodeSubmission, CompletedExercise
from .forms import CodeSubmissionForm

from django.urls import reverse
from quizApp.models import LeaderboardEntry # Add model from the other app
from django.db import transaction #Need transaction!
from django.db.models import Sum, F

@login_required(login_url="login")
@transaction.atomic
def exercise_detail(request, exercise_name):
    exercise = get_object_or_404(Exercise, exercise_name=exercise_name) #Load from name
    has_completed = CompletedExercise.objects.filter(user=request.user, exercise=exercise).exists()
    last_submission = CodeSubmission.objects.filter(user=request.user, exercise=exercise).order_by('-submission_time').first()
    num_attempts = CodeSubmission.objects.filter(user=request.user, exercise=exercise).count() #Get number of attempts
    can_try_again = False #Allow or deny to submit again

    # If the user has already completed the exercise, check if they're allowed to try again
    if has_completed:
        if last_submission and last_submission.score < 50 and num_attempts < 2:
            can_try_again = True
        else:
            return redirect('exerciseApp:submission_detail', exercise_name=exercise.exercise_name) #Access main view
    
    # Create form
    if request.method == 'POST':
        form = CodeSubmissionForm(request.POST)

        # Valid submission: create the objects and check it
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            submission.exercise = exercise

            comparison_result = compare_code(submission.code, exercise.reference_code) # Run similarity and check

            submission.score = comparison_result['score']  # Access the score from the dict
            submission.save() #Set it to the current exercise

            #Check if quiz for adding in QuizSubmission
            #If it exists - it should create an entry
            print(f"Quiz is {exercise.exercise_name}")
            quizzes, created = Quiz.objects.get_or_create(
                quiz_name='exercises',
                defaults={
                    'title': 'Exercise',
                    'description': '',  # Empty description
                    'link': 'link'
                }
            )
            quizzes.save()
            quiz_submission, created = QuizSubmission.objects.get_or_create(user=request.user, quiz=quizzes)
            quiz_submission.total_score = F('total_score') + submission.score
            quiz_submission.save()
            #Update total score in LeaderboardEntry
            try:
                leaderboard_entry = LeaderboardEntry.objects.get(user=request.user)
                leaderboard_entry.total_score = F('total_score') + submission.score
                leaderboard_entry.save()
            except LeaderboardEntry.DoesNotExist:
                LeaderboardEntry.objects.create(user=request.user, total_score=submission.score)

            return redirect('exerciseApp:submission_detail', exercise_name=exercise.exercise_name) #Check main
        else:
            print("Inavlid Form")
    else:
        form = CodeSubmissionForm() #Load main form

    return render(request, 'exercise_detail.html', {
        'exercise': exercise,
        'form': form,
        'num_attempts': num_attempts, #Load the number of attempts
        'can_try_again': can_try_again #Let them load
        })

@login_required(login_url="login")
def submission_detail(request, exercise_name):
    exercise = get_object_or_404(Exercise, exercise_name=exercise_name)
    #Get all the previous code submission
    submission = CodeSubmission.objects.filter(user=request.user, exercise=exercise).order_by('-submission_time').first() #The code
    
    #Load the total score,
    try:
        total_score = LeaderboardEntry.objects.get(user=request.user).total_score
    except:
        total_score = None

    if submission == None: # Error where it does not exist
        return render(request, 'submission_detail.html', {'user': request.user}) #Access view
    else:
        correct_answer = exercise.reference_code #Load reference code
        
        #Example - load all codes or something that makes it work
        data_entries = CodeSubmission.objects.filter(user=request.user)

        leaderboard_entries = LeaderboardEntry.objects.order_by('-total_score')[:10]
        # quizzes = Quiz.objects.filter(quiz_name=exercise_name)
        recent_submission = QuizSubmission.objects.filter(user=request.user).latest('submission_time')
        recent_score = recent_submission.score
        total_score = QuizSubmission.objects.filter(user=request.user).aggregate(Sum('score'))['score__sum'] or 0
        leaderboard = LeaderboardEntry.objects.order_by('-total_score')
        rank = LeaderboardEntry.objects.filter(total_score__gt=LeaderboardEntry.objects.get(user=request.user).total_score).count() + 1
        
        context = {
        'submission': submission,
        'correct_answer': correct_answer, #Show user what the code is
        'total_score': total_score,
        'data_entries': data_entries,
        'leaderboard_entries':leaderboard_entries,
        'leaderboard':leaderboard,
        'rank':rank,
        'recent_score':recent_score,
        } #Add dashboard
        return render(request, 'submission_detail.html', context)
    


#Admin exercise handling
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import SpecialExercise, ExerciseRemarks
from quizApp.models import LeaderboardEntry
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json


@login_required(login_url="login")
def exercises_list(request):
    if request.user.is_staff:
        exercises = SpecialExercise.objects.values('title').distinct()
        return render(request, 'admin_reviews/exercises.html', {
            'exercises': [ex['title'] for ex in exercises]
        })
    else:
        return HttpResponse("You don't have the required permissions to access this page.")

@login_required(login_url="login")
def exercise_submissions(request, exercise_title):
    if request.user.is_staff:
        submissions = SpecialExercise.objects.filter(title=exercise_title, verified=False).select_related('user')
        return render(request, 'admin_reviews/users.html', {
            'exercise_title': exercise_title,
            'submissions': submissions
        })
    else:
        return HttpResponse("You don't have the required permissions to access this page.")


@login_required(login_url="login")
def submission_details(request, submission_id):
    if request.user.is_staff:
        try:
            submission = SpecialExercise.objects.get(id=submission_id)
            print(f"code is {submission.code}")
            # Get existing remarks if they exist
            try:
                remarks = ExerciseRemarks.objects.get(
                    user=submission.user,
                    exercise_title=submission.title
                )
                initial_score = remarks.score
                initial_remarks = remarks.remarks
            except ExerciseRemarks.DoesNotExist:
                initial_score = 0
                initial_remarks = ''
                
            return render(request, 'admin_reviews/submission.html', {
                'submission': submission,
                'initial_score': initial_score,
                'initial_remarks': initial_remarks
            })
        except SpecialExercise.DoesNotExist:
            raise Http404("Exercise submission not found")
    else:
        return HttpResponse("You don't have the required permissions to access this page.")

from django.contrib import messages

@login_required(login_url="login")
@require_POST
def submit_review(request, submission_id):
    submission = get_object_or_404(SpecialExercise, id=submission_id)
    
    if request.user.is_staff:
        try:
            # Create remarks
            ExerciseRemarks.objects.create(
                user=submission.user,
                exercise_title=submission.title,
                remarks=request.POST.get('remarks', ''),
                score=int(request.POST.get('score', 0)),
                code=submission.code  # Save the code with remarks
            )
            
            # Update leaderboard
            leaderboard_entry, created = LeaderboardEntry.objects.get_or_create(
                user=submission.user
            )
            leaderboard_entry.total_score += int(request.POST.get('score', 0))
            leaderboard_entry.save()
            
            # Delete submission if requested
            if request.POST.get('delete'):
                submission.delete()
                messages.success(request, 'Submission deleted successfully.')
            else:
                # Mark as verified
                submission.verified = True
                submission.save()
                messages.success(request, 'Review submitted successfully.')
            
            return redirect('exerciseApp:exercise_submissions', exercise_title=submission.title)
            
        except Exception as e:
            messages.error(request, f'Error submitting review: {str(e)}')
            return redirect('exerciseApp:submission_detail', submission_id=submission.id)
    else:
        return HttpResponse("You don't have the required permissions to access this page.")
    


@login_required(login_url="login")
def user_reviews(request):
    # Get all reviews for the current user
    reviews = ExerciseRemarks.objects.filter(user=request.user).order_by('-date')
    pending_submissions = SpecialExercise.objects.filter(user=request.user, verified=False).order_by('-date')
    return render(request, 'user_reviews/user_reviews.html', {
        'reviews': reviews,
        'pending_submissions':pending_submissions
    })
    