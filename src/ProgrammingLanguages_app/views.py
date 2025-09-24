from django.shortcuts import render, get_object_or_404
from .models import PogrammingLanguage
from quizApp.views import *
from introToHTML_app.views import require_special_exercise_submission_HTML
from introToCSS_app.views import require_special_exercise_submission_CSS
from blog_ttrial.views import require_special_exercise_submission_blog_ex2,require_special_exercise_submission_blog_ex3,require_special_exercise_submission_blog_ex4
from django.http import HttpResponse
from exerciseApp.models import SpecialExercise
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# javascript views javascript views javascript views javascript views javascript views javascript views javascript views
# javascript views javascript views javascript views javascript views javascript views javascript views javascript views


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page1(request):
    return render(request, 'javaScript/code/js_page1.html')


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page2(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript2.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript2.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript2.3')
    code_4=PogrammingLanguage.objects.filter(title='javaScript2.4')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'javaScript/code/js_page2.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page3(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript3.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript3.2')

    context={
        'code_1':code_1,
        'code_2':code_2,
    }
    return render(request, 'javaScript/code/js_page3.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page4(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript4.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript4.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript4.3')
    code_4=PogrammingLanguage.objects.filter(title='javaScript4.4')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'javaScript/code/js_page4.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page5(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript5.1')
    quiz = get_object_or_404(Quiz, quiz_name='JSQ1')
    #check if the user has already submitted an answer for the quiz
    has_answered = QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()

    context={
        'code_1':code_1,
        'has_answered':has_answered,
    }
    return render(request, 'javaScript/code/js_page5.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page6(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript6.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript6.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript6.3')
    code_4=PogrammingLanguage.objects.filter(title='javaScript6.4')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'javaScript/code/js_page6.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page7(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript7.1')

    context={
        'code_1':code_1,
    }
    return render(request, 'javaScript/code/js_page7.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page8(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript8.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript8.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript8.3')
    code_4=PogrammingLanguage.objects.filter(title='javaScript8.4')
    
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'javaScript/code/js_page8.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page9(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript9.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript9.2')

    context={
        'code_1':code_1,
        'code_2':code_2,
    }
    return render(request, 'javaScript/code/js_page9.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page10(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript10.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript10.2')

    quiz = get_object_or_404(Quiz, quiz_name='JSQ2')
    #check if the user has already submitted an answer for the quiz
    has_answered = QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()

    context={
        'code_1':code_1,
        'code_2':code_2,
        'has_answered':has_answered
    }
    return render(request, 'javaScript/code/js_page10.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page11(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript11.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript11.2')

    context={
        'code_1':code_1,
        'code_2':code_2,
    }
    return render(request, 'javaScript/code/js_page11.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page12(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript12.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript12.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript12.3')

    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
    }
    return render(request, 'javaScript/code/js_page12.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page13(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript13.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript13.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript13.3')

    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
    }
    return render(request, 'javaScript/code/js_page13.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page14(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript14.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript14.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript14.3')
    code_4=PogrammingLanguage.objects.filter(title='javaScript14.4')

    quiz = get_object_or_404(Quiz, quiz_name='JSQ3')
    #check if the user has already submitted an answer for the quiz
    has_answered = QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()

    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'has_answered':has_answered,
    }
    return render(request, 'javaScript/code/js_page14.html', context)



@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page15(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript15.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript15.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript15.3')
    code_4=PogrammingLanguage.objects.filter(title='javaScript15.4')

    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'javaScript/code/js_page15.html', context)



@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page16(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript16.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript16.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript16.3')
    code_4=PogrammingLanguage.objects.filter(title='javaScript16.4')

    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'javaScript/code/js_page16.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page17(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript17.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript17.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript17.3')
    code_4=PogrammingLanguage.objects.filter(title='javaScript17.4')

    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'javaScript/code/js_page17.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page18(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript18.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript18.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript18.3')
    code_4=PogrammingLanguage.objects.filter(title='javaScript18.4')

    quiz = get_object_or_404(Quiz, quiz_name='JSQ4')
    #check if the user has already submitted an answer for the quiz
    has_answered = QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()

    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'has_answered':has_answered,
    }
    return render(request, 'javaScript/code/js_page18.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page19(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript19.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript19.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript19.3')
    code_4=PogrammingLanguage.objects.filter(title='javaScript19.4')

    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'javaScript/code/js_page19.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page20(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript20.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript20.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript20.3')
    code_4=PogrammingLanguage.objects.filter(title='javaScript20.4')

    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'javaScript/code/js_page20.html', context)



@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page21(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript21.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript21.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript21.3')
    code_4=PogrammingLanguage.objects.filter(title='javaScript21.4')

    quiz = get_object_or_404(Quiz, quiz_name='JSQ5')
    #check if the user has already submitted an answer for the quiz
    has_answered = QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()

    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'has_answered':has_answered,
    }
    return render(request, 'javaScript/code/js_page21.html', context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def js_page22(request):
    code_1=PogrammingLanguage.objects.filter(title='javaScript22.1')
    code_2=PogrammingLanguage.objects.filter(title='javaScript22.2')
    code_3=PogrammingLanguage.objects.filter(title='javaScript22.3')
    code_4=PogrammingLanguage.objects.filter(title='javaScript22.4')

    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'javaScript/code/js_page22.html', context)


# python views python views python views python views python views python views python views python views python views python views 
# python views python views python views python views python views python views python views python views python views python views 



def py_page1(request):
    return render(request, 'python/code/py_page1.html')

def py_page2(request):
    code_1=PogrammingLanguage.objects.filter(title='python2.1')
    code_2=PogrammingLanguage.objects.filter(title='python2.2')
    code_3=PogrammingLanguage.objects.filter(title='python2.3')
    code_4=PogrammingLanguage.objects.filter(title='python2.4')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'python/code/py_page2.html', context)

def py_page3(request):
    code_1=PogrammingLanguage.objects.filter(title='python3.1')
    code_2=PogrammingLanguage.objects.filter(title='python3.2')
    code_3=PogrammingLanguage.objects.filter(title='python3.3')
    code_4=PogrammingLanguage.objects.filter(title='python3.4')
    code_5=PogrammingLanguage.objects.filter(title='python3.5')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
    }
    return render(request, 'python/code/py_page3.html', context)

def py_page4(request):
    code_1=PogrammingLanguage.objects.filter(title='python4.1')
    code_2=PogrammingLanguage.objects.filter(title='python4.2')
    code_3=PogrammingLanguage.objects.filter(title='python4.3')
    code_4=PogrammingLanguage.objects.filter(title='python4.4')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'python/code/py_page4.html', context)

def py_page5(request):
    code_1=PogrammingLanguage.objects.filter(title='python5.1')
    code_2=PogrammingLanguage.objects.filter(title='python5.2')
    code_3=PogrammingLanguage.objects.filter(title='python5.3')
    code_4=PogrammingLanguage.objects.filter(title='python5.4')
    
    quiz = get_object_or_404(Quiz, quiz_name='PYQ1')
    #check if the user has already submitted an answer for the quiz
    has_answered = QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'has_answered':has_answered,
    }
    return render(request, 'python/code/py_page5.html', context)

def py_page6(request):
    code_1=PogrammingLanguage.objects.filter(title='python6.1')
    code_2=PogrammingLanguage.objects.filter(title='python6.2')
    code_3=PogrammingLanguage.objects.filter(title='python6.3')
    code_4=PogrammingLanguage.objects.filter(title='python6.4')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'python/code/py_page6.html', context)

def py_page7(request):
    code_1=PogrammingLanguage.objects.filter(title='python7.1')
    code_2=PogrammingLanguage.objects.filter(title='python7.2')
    code_3=PogrammingLanguage.objects.filter(title='python7.3')
    code_4=PogrammingLanguage.objects.filter(title='python7.4')
    code_5=PogrammingLanguage.objects.filter(title='python7.5')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
    }
    return render(request, 'python/code/py_page7.html', context)

def py_page8(request):
    code_1=PogrammingLanguage.objects.filter(title='python8.1')
    code_2=PogrammingLanguage.objects.filter(title='python8.2')
    code_3=PogrammingLanguage.objects.filter(title='python8.3')
    code_4=PogrammingLanguage.objects.filter(title='python8.4')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
    }
    return render(request, 'python/code/py_page8.html', context)

def py_page9(request):
    code_1=PogrammingLanguage.objects.filter(title='python9.1')
    code_2=PogrammingLanguage.objects.filter(title='python9.2')
    code_3=PogrammingLanguage.objects.filter(title='python9.3')
    code_4=PogrammingLanguage.objects.filter(title='python9.4')
    code_5=PogrammingLanguage.objects.filter(title='python9.5')

    quiz = get_object_or_404(Quiz, quiz_name='PYQ2')
    #check if the user has already submitted an answer for the quiz
    has_answered = QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
        'has_answered':has_answered,
    }
    return render(request, 'python/code/py_page9.html', context)

def py_page9b(request):
    code_1=PogrammingLanguage.objects.filter(title='python9b.1')
    code_2=PogrammingLanguage.objects.filter(title='python9b.2')
    code_3=PogrammingLanguage.objects.filter(title='python9b.3')
    code_4=PogrammingLanguage.objects.filter(title='python9b.4')
    code_5=PogrammingLanguage.objects.filter(title='python9b.5')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
    }
    return render(request, 'python/code/py_page9b.html', context)

def py_page10(request):
    code_1=PogrammingLanguage.objects.filter(title='python10.1')
    code_2=PogrammingLanguage.objects.filter(title='python10.2')
    code_3=PogrammingLanguage.objects.filter(title='python10.3')
    code_4=PogrammingLanguage.objects.filter(title='python10.4')
    code_5=PogrammingLanguage.objects.filter(title='python10.5')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
    }
    return render(request, 'python/code/py_page10.html', context)

def py_page11(request):
    code_1=PogrammingLanguage.objects.filter(title='python11.1')
    code_2=PogrammingLanguage.objects.filter(title='python11.2')
    code_3=PogrammingLanguage.objects.filter(title='python11.3')
    code_4=PogrammingLanguage.objects.filter(title='python11.4')
    code_5=PogrammingLanguage.objects.filter(title='python11.5')

    quiz = get_object_or_404(Quiz, quiz_name='PYQ3')
    #check if the user has already submitted an answer for the quiz
    has_answered = QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
        'has_answered':has_answered,
    }
    return render(request, 'python/code/py_page11.html', context)

def py_page12(request):
    code_1=PogrammingLanguage.objects.filter(title='python12.1')
    code_2=PogrammingLanguage.objects.filter(title='python12.2')
    code_3=PogrammingLanguage.objects.filter(title='python12.3')
    code_4=PogrammingLanguage.objects.filter(title='python12.4')
    code_5=PogrammingLanguage.objects.filter(title='python12.5')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
    }
    return render(request, 'python/code/py_page12.html', context)

def py_page13(request):
    code_1=PogrammingLanguage.objects.filter(title='python13.1')
    code_2=PogrammingLanguage.objects.filter(title='python13.2')
    code_3=PogrammingLanguage.objects.filter(title='python13.3')
    code_4=PogrammingLanguage.objects.filter(title='python13.4')
    code_5=PogrammingLanguage.objects.filter(title='python13.5')

    quiz = get_object_or_404(Quiz, quiz_name='PYQ4')
    #check if the user has already submitted an answer for the quiz
    has_answered = QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()

    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
        'has_answered':has_answered,
    }
    return render(request, 'python/code/py_page13.html', context)

def py_page14(request):
    code_1=PogrammingLanguage.objects.filter(title='python14.1')
    code_2=PogrammingLanguage.objects.filter(title='python14.2')
    code_3=PogrammingLanguage.objects.filter(title='python14.3')
    code_4=PogrammingLanguage.objects.filter(title='python14.4')
    code_5=PogrammingLanguage.objects.filter(title='python14.5')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
    }
    return render(request, 'python/code/py_page14.html', context)

def py_page14b(request):
    code_1=PogrammingLanguage.objects.filter(title='python14b.1')
    code_2=PogrammingLanguage.objects.filter(title='python14b.2')
    code_3=PogrammingLanguage.objects.filter(title='python14b.3')
    code_4=PogrammingLanguage.objects.filter(title='python14b.4')
    code_5=PogrammingLanguage.objects.filter(title='python14b.5')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
    }
    return render(request, 'python/code/py_page14b.html', context)

def py_page14c(request):
    code_1=PogrammingLanguage.objects.filter(title='python14c.1')
    code_2=PogrammingLanguage.objects.filter(title='python14c.2')
    code_3=PogrammingLanguage.objects.filter(title='python14c.3')
    code_4=PogrammingLanguage.objects.filter(title='python14c.4')
    code_5=PogrammingLanguage.objects.filter(title='python14c.5')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
    }
    return render(request, 'python/code/py_page14c.html', context)

def py_page14d(request):
    code_1=PogrammingLanguage.objects.filter(title='python14d.1')
    code_2=PogrammingLanguage.objects.filter(title='python14d.2')
    code_3=PogrammingLanguage.objects.filter(title='python14d.3')
    code_4=PogrammingLanguage.objects.filter(title='python14d.4')
    code_5=PogrammingLanguage.objects.filter(title='python14d.5')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
    }
    return render(request, 'python/code/py_page14d.html', context)


def py_page15(request):
    code_1=PogrammingLanguage.objects.filter(title='python15.1')
    code_2=PogrammingLanguage.objects.filter(title='python15.2')
    code_3=PogrammingLanguage.objects.filter(title='python15.3')
    code_4=PogrammingLanguage.objects.filter(title='python15.4')
    code_5=PogrammingLanguage.objects.filter(title='python15.5')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
    }
    return render(request, 'python/code/py_page15.html', context)

def py_page16(request):
    code_1=PogrammingLanguage.objects.filter(title='python16.1')
    code_2=PogrammingLanguage.objects.filter(title='python16.2')
    code_3=PogrammingLanguage.objects.filter(title='python16.3')
    code_4=PogrammingLanguage.objects.filter(title='python16.4')
    code_5=PogrammingLanguage.objects.filter(title='python16.5')

    quiz = get_object_or_404(Quiz, quiz_name='PYQ5')
    #check if the user has already submitted an answer for the quiz
    has_answered = QuizSubmission.objects.filter(user=request.user, quiz=quiz).exists()
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
        'code_4':code_4,
        'code_5':code_5,
        'has_answered':has_answered,
    }
    return render(request, 'python/code/py_page16.html', context)




