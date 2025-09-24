from django.shortcuts import render,redirect,get_object_or_404
from .models import IntroToCSS
from introToHTML_app.views import require_special_exercise_submission_HTML
from django.http import HttpResponse
from quizApp.models import QuizSubmission,Quiz
from exerciseApp.models import SpecialExercise
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
@require_special_exercise_submission_HTML
def introduction_to_cssView(request):
    return render(request, 'Intro_To_CSS/introduction_to_css.html')

@login_required(login_url="login")
@require_special_exercise_submission_HTML
def CSS_intro_page1(request):
    code=IntroToCSS.objects.filter(title='CSS_1.1')
    context={
        'code':code
    }
    return render(request, 'Intro_To_CSS/css_page1.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
def CSS_intro_page2(request):

    return render(request, 'Intro_To_CSS/css_page2.html')

@login_required(login_url="login")
@require_special_exercise_submission_HTML
def CSS_intro_page3(request):
    quiz = get_object_or_404(Quiz, quiz_name='CSSQ1')
    #check if the user has already submitted an answer for the quiz
    has_answered = QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()

    return render(request, 'Intro_To_CSS/css_page3.html',{'has_answered':has_answered})

@login_required(login_url="login")
@require_special_exercise_submission_HTML
def CSS_intro_page4(request):

    return render(request, 'Intro_To_CSS/css_page4.html')

@login_required(login_url="login")
@require_special_exercise_submission_HTML
def CSS_intro_page5(request):

    quiz = get_object_or_404(Quiz, quiz_name='CSSQ2')
    #check if the user has already submitted an answer for the quiz
    has_answered = QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()
    return render(request, 'Intro_To_CSS/css_page5.html',{'has_answered':has_answered})


@login_required(login_url="login")
@require_special_exercise_submission_HTML
def CSS_intro_page6(request):

    return render(request, 'Intro_To_CSS/css_page6.html')

@login_required(login_url="login")
@require_special_exercise_submission_HTML
def CSS_intro_page7(request):
    code=IntroToCSS.objects.filter(title='CSS_7.1')
    quiz = get_object_or_404(Quiz, quiz_name='CSSQ2')
    #check if the user has already submitted an answer for the quiz
    has_answered = QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()

    context={
        'code':code,
        'has_answered':has_answered
    }
    return render(request, 'Intro_To_CSS/css_page7.html', context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
def CSSIntro_ex1(request):
    return render(request, 'Intro_To_CSS/exercise-1.html')

@login_required(login_url="login")
@require_special_exercise_submission_HTML
def CSSIntro_ex2(request):
    return render(request, 'Intro_To_CSS/exercise-2.html')

@login_required(login_url="login")
@require_special_exercise_submission_HTML
def CSSIntro_ex3(request):
    has_submitted=SpecialExercise.objects.filter(user=request.user,title="CSS Exercise 3") #checks if a user has done the exercise
    return render(request, 'Intro_To_CSS/exercise-3.html',{'has_submitted':has_submitted})


#The logic below checks whether a user has submitted their exercise

from functools import wraps

def require_special_exercise_submission_CSS(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            SpecialExercise.objects.get(user=request.user,title="CSS Exercise 3")
        except SpecialExercise.DoesNotExist:
            messages.error(request, 'You must complete this Exercise before you can proceed.')
            return redirect('css_ex3')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@login_required(login_url="login")
@require_special_exercise_submission_HTML
def Exercise3_submission(request):
    user=request.user
    try:
        has_submitted=SpecialExercise.objects.filter(user=request.user,title="CSS Exercise 3") #checks if a user has done the exercise
        if request.method == 'POST':
            if not has_submitted:
                    title=request.POST.get('title')
                    lang = request.POST.get('type')
                    code = request.POST.get('code')
                    special_exercise = SpecialExercise(user=user, title=title, type=lang, code=code, verified=False)
                    special_exercise.save()
                    return redirect('CSS_SuccessView')
            else:
                return HttpResponse("You can't submitted thesame exercise twice.")
        else:
            return render(request, 'Intro_To_CSS/css_ex3_submission.html',{'has_submitted':has_submitted})
        
    except:
        return HttpResponse("Something went wrong")
    
@login_required(login_url="login")
@require_special_exercise_submission_HTML    
def CSS_SuccessView(request):
    return render(request, 'Intro_To_CSS/success.html')


    


