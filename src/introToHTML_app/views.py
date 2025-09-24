from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import HttpResponse
from exerciseApp.models import SpecialExercise
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from functools import wraps
from quizApp.views import QuizSubmission
from quizApp.models import Quiz

# Create your views here.

# def index_view(request):
#     return render(request,'IntroToHTML/index.html')


def page1_view(request):

    return render(request,'IntroToHTML/page1.html')

@login_required(login_url="login")
def page2_view(request):
    return render(request,'IntroToHTML/page2.html')

@login_required(login_url="login")
def page3_view(request):
    return render(request,'IntroToHTML/page3.html')

@login_required(login_url="login")
def page4_view(request):
    context=IntroToHTML.objects.filter(title='HTML_intro2')
    return render(request,'IntroToHTML/page4.html',{'code':context})

@login_required(login_url="login")
def HTMLIntro_ex2(request):
    return render(request, 'IntroToHTML/exercise-2.html')

@login_required(login_url="login") 
def page5_view(request):
    context=IntroToHTML.objects.filter(title='HTML_intro5')
    quiz = get_object_or_404(Quiz, quiz_name='HTMLQ1')
    #check if the user has already submitted an answer for the quiz
    if request.user.is_anonymous:
        has_answered=True
    else:
        has_answered=QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()
        print(f"Does the Quiz exist?: {has_answered}")


    return render(request,'IntroToHTML/page5.html',{'code':context,'has_answered':has_answered})

@login_required(login_url="login")
def page5b_view(request):
    context=IntroToHTML.objects.filter(title='HTML_intro5b')
    return render(request,'IntroToHTML/page5b.html',{'code':context})

@login_required(login_url="login")
def page6_view(request):
    code_1=IntroToHTML.objects.filter(title='HTML_intro6.1')
    code_2=IntroToHTML.objects.filter(title='HTML_intro6.2')
    code_3=IntroToHTML.objects.filter(title='HTML_intro6.3')
    code_4=IntroToHTML.objects.filter(title='HTML_intro6.4')
    quiz = get_object_or_404(Quiz, quiz_name='HTMLQ2')
    #check if the user has already submitted an answer for the quiz
    if request.user.is_anonymous:
        has_answered=True
    else:
        has_answered=QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()
    # if request.user.is_anonymous:
    #     has_answered=True
    # else:
    #     has_answered=QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()


    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'has_answered':has_answered,
    }
    return render(request,'IntroToHTML/page6.html',context)

@login_required(login_url="login")
def page6b_view(request):
    code_1=IntroToHTML.objects.filter(title='HTML_intro6b.1')
    code_2=IntroToHTML.objects.filter(title='HTML_intro6b.2')
    code_3=IntroToHTML.objects.filter(title='HTML_intro6b.3')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
    }
    return render(request,'IntroToHTML/page6b.html',context)

@login_required(login_url="login")
def page7_view(request):
    code_1=IntroToHTML.objects.filter(title='HTML_intro7.1')
    code_2=IntroToHTML.objects.filter(title='HTML_intro7.2')
    code_3=IntroToHTML.objects.filter(title='HTML_intro7.3')
    code_4=IntroToHTML.objects.filter(title='HTML_intro7.4')
    quiz = get_object_or_404(Quiz, quiz_name='HTMLQ3')
    #check if the user has already submitted an answer for the quiz
    if request.user.is_anonymous:
        has_answered=True
    else:
        has_answered=QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()


    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'has_answered':has_answered,
    }
    return render(request,'IntroToHTML/page7.html',context)

@login_required(login_url="login")
def page7b_view(request):
    code_1=IntroToHTML.objects.filter(title='HTML_intro7b.1')
    code_2=IntroToHTML.objects.filter(title='HTML_intro7b.2')
    code_3=IntroToHTML.objects.filter(title='HTML_intro7b.3')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
    }
    return render(request,'IntroToHTML/page7b.html',context)

@login_required(login_url="login")
def page8_view(request):
    code_1=IntroToHTML.objects.filter(title='HTML_intro8.1')
    code_2=IntroToHTML.objects.filter(title='HTML_intro8.2')
    code_3=IntroToHTML.objects.filter(title='HTML_intro8.3')
    code_4=IntroToHTML.objects.filter(title='HTML_intro8.4')
    code_5=IntroToHTML.objects.filter(title='HTML_intro8.5')
    code_6=IntroToHTML.objects.filter(title='HTML_intro8.6')
    code_7=IntroToHTML.objects.filter(title='HTML_intro8.7')
    code_8=IntroToHTML.objects.filter(title='HTML_intro8.8')
    quiz = get_object_or_404(Quiz, quiz_name='HTMLQ4')
    #check if the user has already submitted an answer for the quiz
    if request.user.is_anonymous:
        has_answered=True
    else:
        has_answered=QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()


    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
        'code_6':code_6,
        'code_7':code_7,
        'code_8':code_8,
        'has_answered':has_answered,

    }
    return render(request, 'IntroToHTML/page8.html',context)

@login_required(login_url="login")
def HTMLIntro_ex1(request):
    return render(request, 'IntroToHTML/exercise-1.html')

@login_required(login_url="login")
def HTMLIntro_ex2(request):
    return render(request, 'IntroToHTML/exercise-2.html')

@login_required(login_url="login")
def HTMLIntro_ex3(request):
    return render(request, 'IntroToHTML/exercise-3.html')

@login_required(login_url="login")
def HTMLIntro_ex4(request):
    return render(request, 'IntroToHTML/exercise-4.html')

@login_required(login_url="login")  
def HTMLIntro_ex5(request):
    code=IntroToHTML.objects.filter(title='HTML_intro_ex5')
    has_submitted=SpecialExercise.objects.filter(user=request.user,title="HTML Exercise 5").exists()#checks if a user has done the exercise
    print(f"Has submitted?: {has_submitted}")

    return render(request, 'IntroToHTML/exercise-5.html',{'code':code, 'has_submitted':has_submitted})

from functools import wraps

def require_special_exercise_submission_HTML(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            SpecialExercise.objects.get(user=request.user,title="HTML Exercise 5")
        except SpecialExercise.DoesNotExist:
            messages.error(request, 'You must complete this Exercise before you can proceed.')
            return redirect('HTMLIntro_ex5')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@login_required(login_url="login")
def Exercise5_submission(request): 
    user=request.user
    if user.is_authenticated:
        try:
            has_submitted=SpecialExercise.objects.filter(user=request.user,title="HTML Exercise 5") #checks if a user has done the exercise
            if request.method == 'POST':
                if not has_submitted:
                        title="HTML Exercise 5"
                        print(f'title is {title}')
                        lang = "HTML"
                        print(f'lang is {lang}')
                        code = request.POST.get('code')
                        print(f'code is {code}')
                        special_exercise = SpecialExercise(user=user, title=title, type=lang, code=code, verified=False)
                        special_exercise.save()
                        return redirect('HTML_SuccessView')
                else:
                    return HttpResponse("You can't submitted thesame exercise twice.")
            else:
                return render(request, 'IntroToHTML/exercise5_submission.html', {'has_submitted':has_submitted})
            
        
        except:
            return HttpResponse("Something went wrong")
    else:
        return HttpResponse("Something went wrong")
        


    
    
@login_required(login_url="login")    
def HTML_SuccessView(request):
    return render(request, 'IntroToHTML/success.html')


    