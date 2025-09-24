from django.shortcuts import render, redirect
from .models import BlogTTrial
from introToHTML_app.views import require_special_exercise_submission_HTML
from introToCSS_app.views import require_special_exercise_submission_CSS
from django.http import HttpResponse
from exerciseApp.models import SpecialExercise
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page1(request):
    return render(request, 'blog_ttrial/page1.html')

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page2(request):
    return render(request, 'blog_ttrial/page2.html')

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page3(request):
    context=BlogTTrial.objects.filter(title='blogP3_HTML1')
    return render(request, 'blog_ttrial/page3.html',{'code':context})

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page4(request):
    code_1=BlogTTrial.objects.filter(title='blogP4_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP4_HTML1a')
    context={
        'code_1':code_1,
        'code_1a':code_1a,
    }
    return render(request, 'blog_ttrial/page4.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page5(request):
    code_1=BlogTTrial.objects.filter(title='blogP5_CSS1')
    code_2=BlogTTrial.objects.filter(title='blogP5_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP5_CSS2a')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_2a':code_2a,
    }
    return render(request, 'blog_ttrial/page5.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page6(request):
    code_1=BlogTTrial.objects.filter(title='blogP6_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP6_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP6_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP6_CSS2a')
    code_3=BlogTTrial.objects.filter(title='blogP6_CSS3')
    code_3a=BlogTTrial.objects.filter(title='blogP6_CSS3a')
    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,
        'code_3':code_3,
        'code_3a':code_3a,
    }
    return render(request, 'blog_ttrial/page6.html',context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page7(request):
    code_1=BlogTTrial.objects.filter(title='blogP7_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP7_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP7_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP7_CSS2a')
    code_3=BlogTTrial.objects.filter(title='blogP7_CSS3')
    code_3a=BlogTTrial.objects.filter(title='blogP7_CSS3a')
    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,
        'code_3':code_3,
        'code_3a':code_3a,
    }
    return render(request, 'blog_ttrial/page7.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page8(request):
    code_1=BlogTTrial.objects.filter(title='blogP8_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP8_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP8_CSS2')
    code_3=BlogTTrial.objects.filter(title='blogP8_CSS3')
    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_3':code_3,
    }
    return render(request, 'blog_ttrial/page8.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page9(request):
    code_1=BlogTTrial.objects.filter(title='blogP8_HTML1')
    
    context={
        'code_1':code_1,
    }
    return render(request, 'blog_ttrial/page9.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page10(request):
    code_1=BlogTTrial.objects.filter(title='blogP10_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP10_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP10_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP10_CSS2a')
    code_3=BlogTTrial.objects.filter(title='blogP10_CSS3')
    code_3a=BlogTTrial.objects.filter(title='blogP10_CSS3a')
    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,
        'code_3':code_3,
        'code_3a':code_3a,
    }
    return render(request, 'blog_ttrial/page10.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page11(request):
    code_1=BlogTTrial.objects.filter(title='blogP11_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP11_HTML1a')
    code_2=BlogTTrial.objects.filter(title='blogP11_HTML2')
    code_2a=BlogTTrial.objects.filter(title='blogP11_HTML2a')
    code_3=BlogTTrial.objects.filter(title='blogP11_CSS3')
    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,
        'code_3':code_3,
    }
    return render(request, 'blog_ttrial/page11.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page12(request):
    code_1=BlogTTrial.objects.filter(title='blogP12_CSS1')
    code_2=BlogTTrial.objects.filter(title='blogP12_CSS2')
    code_3=BlogTTrial.objects.filter(title='blogP12_CSS3')
    context={
        'code_1':code_1,
        'code_2':code_2,
        'code_3':code_3,
    }
    return render(request, 'blog_ttrial/page12.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page13(request):
    code_1=BlogTTrial.objects.filter(title='blogP13_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP13_HTML1a')
    code_2=BlogTTrial.objects.filter(title='blogP13_HTML2')
    code_2a=BlogTTrial.objects.filter(title='blogP13_HTML2a')
    code_3=BlogTTrial.objects.filter(title='blogP13_HTML3')
    code_3a=BlogTTrial.objects.filter(title='blogP13_HTML3a')
    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,
        'code_3':code_3,
        'code_3a':code_3a,
    }
    return render(request, 'blog_ttrial/page13.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page14(request):
    code_1=BlogTTrial.objects.filter(title='blogP14_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP14_HTML1a')
    code_2=BlogTTrial.objects.filter(title='blogP14_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP14_CSS2a')
    code_3=BlogTTrial.objects.filter(title='blogP14_HTML3')
    code_3a=BlogTTrial.objects.filter(title='blogP14_HTML3a')
    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,
        'code_3':code_3,
        'code_3a':code_3a,
    }
    return render(request, 'blog_ttrial/page14.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page15(request):
    code_1=BlogTTrial.objects.filter(title='blogP15_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP15_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP15_HTML2')
    code_2a=BlogTTrial.objects.filter(title='blogP15_HTML2a')
    code_3=BlogTTrial.objects.filter(title='blogP15_CSS3')
    code_3a=BlogTTrial.objects.filter(title='blogP15_CSS3a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,
        'code_3':code_3,
        'code_3a':code_3a,
        
    }
    return render(request, 'blog_ttrial/page15.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page16(request):
    code_1=BlogTTrial.objects.filter(title='blogP16_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP16_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP16_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP16_CSS2a')
    code_3=BlogTTrial.objects.filter(title='blogP16_CSS3')
    code_3a=BlogTTrial.objects.filter(title='blogP16_CSS3a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,
        'code_3':code_3,
        'code_3a':code_3a,
        
    }
    return render(request, 'blog_ttrial/page16.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page17(request):
    code_1=BlogTTrial.objects.filter(title='blogP17_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP17_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP17_HTML2')
    code_2a=BlogTTrial.objects.filter(title='blogP17_HTML2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,
        
    }
    return render(request, 'blog_ttrial/page17.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page18(request):
    return render(request, 'blog_ttrial/page18.html')

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page19(request):
    code_1=BlogTTrial.objects.filter(title='blogP19_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP19_HTML1a')
    return render(request, 'blog_ttrial/page19.html',{'code_1':code_1, 'code_1a':code_1a})

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page20(request):
    code_1=BlogTTrial.objects.filter(title='blogP20_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP20_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP20_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP20_CSS2a')
    code_3=BlogTTrial.objects.filter(title='blogP20_CSS3')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,
        
    }
    return render(request, 'blog_ttrial/page20.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page21(request):
    code_1=BlogTTrial.objects.filter(title='blogP21_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP21_HTML1a')
    code_2=BlogTTrial.objects.filter(title='blogP21_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP21_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,    
    }
    return render(request, 'blog_ttrial/page21.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page22(request):
    code_1=BlogTTrial.objects.filter(title='blogP22_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP22_HTML1a')
    code_2=BlogTTrial.objects.filter(title='blogP22_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP22_CSS2a')


    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,      
    }
    return render(request, 'blog_ttrial/page22.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page23(request):
    code_1=BlogTTrial.objects.filter(title='blogP23_HTML1')
    code_2=BlogTTrial.objects.filter(title='blogP23_CSS2')

    context={
        'code_1':code_1,
        'code_2':code_2,     
    }
    return render(request, 'blog_ttrial/page23.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page24(request):
    code_1=BlogTTrial.objects.filter(title='blogP24_HTML1')
    code_2=BlogTTrial.objects.filter(title='blogP24_CSS2')

    context={
        'code_1':code_1,
        'code_2':code_2,     
    }
    return render(request, 'blog_ttrial/page24.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page25(request):
    return render(request, 'blog_ttrial/page25.html')

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page26(request):
    has_submitted=SpecialExercise.objects.filter(user=request.user,title="Blog Exercise 2") #checks if a user has done the exercise
    return render(request, 'blog_ttrial/page26.html',{'has_submitted':has_submitted})

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
def blogApp_page26_b(request):
    return render(request, 'blog_ttrial/page26_b.html')

from functools import wraps

def require_special_exercise_submission_blog_ex2(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            SpecialExercise.objects.get(user=request.user,title="Blog Exercise 2")
        except SpecialExercise.DoesNotExist:
            messages.error(request, 'You must complete this Exercise before you can proceed. Submit your result using internal CSS.')
            return redirect('blog_pg26')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@login_required(login_url="login")
def blog_ex2_submission(request):
    user=request.user
    try:
        has_submitted=SpecialExercise.objects.filter(user=request.user,title="Blog Exercise 2") #checks if a user has done the exercise
        if request.method == 'POST':
            if not has_submitted:
                    title=request.POST.get('title')
                    lang = request.POST.get('type')
                    code = request.POST.get('code')
                    special_exercise = SpecialExercise(user=user, title=title, type=lang, code=code, verified=False)
                    special_exercise.save()
                    return redirect('blog_ex2_SuccessView')
            else:
                return HttpResponse("You can't submitted thesame exercise twice.")
        else:
            return render(request, 'blog_ttrial/blog_ex2_submission.html', {'has_submitted':has_submitted})
        
        
    except:
        return HttpResponse("Something went wrong")
    
@login_required(login_url="login")    
def blog_ex2_SuccessView(request):
    return render(request, 'blog_ttrial/exercise2_success.html')


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page27(request):
    code_1=BlogTTrial.objects.filter(title='blogP27_HTML1')
    code_2=BlogTTrial.objects.filter(title='blogP27_CSS2')

    context={
        'code_1':code_1,
        'code_2':code_2,     
    }
    return render(request, 'blog_ttrial/page27.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page27_b(request):
    return render(request, 'blog_ttrial/page27_b.html')

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page28(request):
    code_1=BlogTTrial.objects.filter(title='blogP28_HTML1')
    code_2=BlogTTrial.objects.filter(title='blogP28_CSS2')

    context={
        'code_1':code_1,
        'code_2':code_2,      
    }
    return render(request, 'blog_ttrial/page28.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page29(request):
    code_1=BlogTTrial.objects.filter(title='blogP29_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP29_HTML1a')
    code_2=BlogTTrial.objects.filter(title='blogP29_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP29_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,  
        'code_2a':code_2a,   
    }
    return render(request, 'blog_ttrial/page29.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page30(request):
    code_1=BlogTTrial.objects.filter(title='blogP30_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP30_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP30_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP30_CSS2a')
    code_3=BlogTTrial.objects.filter(title='blogP30_CSS3')
    code_3a=BlogTTrial.objects.filter(title='blogP30_CSS3a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,    
        'code_3':code_3,
        'code_3a':code_3a,   
    }
    return render(request, 'blog_ttrial/page30.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page31(request):
    code_1=BlogTTrial.objects.filter(title='blogP31_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP31_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP31_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP31_CSS2a')
    code_3=BlogTTrial.objects.filter(title='blogP31_CSS3')
    code_3a=BlogTTrial.objects.filter(title='blogP31_CSS3a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2, 
        'code_2a':code_2a,  
        'code_3':code_3, 
        'code_3a':code_3a,  
    }
    return render(request, 'blog_ttrial/page31.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page32(request):
    code_1=BlogTTrial.objects.filter(title='blogP32_CSS1')

    context={
        'code_1':code_1,   
    }
    return render(request, 'blog_ttrial/page32.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page33(request):
    code_1=BlogTTrial.objects.filter(title='blogP33_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP33_HTML1a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,      
    }
    return render(request, 'blog_ttrial/page33.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page34(request):
    code_1=BlogTTrial.objects.filter(title='blogP34_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP34_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP34_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP34_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,      
    }
    return render(request, 'blog_ttrial/page34.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page35(request):
    code_1=BlogTTrial.objects.filter(title='blogP35_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP35_CSS1a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,       
    }
    return render(request, 'blog_ttrial/page35.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page36(request):
    code_1=BlogTTrial.objects.filter(title='blogP36_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP36_HTML1a')
    code_2=BlogTTrial.objects.filter(title='blogP36_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP36_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,     
    }
    return render(request, 'blog_ttrial/page36.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page37(request):
    code_1=BlogTTrial.objects.filter(title='blogP37_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP37_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP37_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP37_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,      
    }
    return render(request, 'blog_ttrial/page37.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page38(request):
    return render(request, 'blog_ttrial/page38.html')

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
def blogApp_page39(request):
    has_submitted=SpecialExercise.objects.filter(user=request.user,title="Blog Exercise 3") #checks if a user has done the exercise
    return render(request, 'blog_ttrial/page39.html', {'has_submitted':has_submitted})

#Excercise 3 logic
from functools import wraps

def require_special_exercise_submission_blog_ex3(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            SpecialExercise.objects.filter(user=request.user,title="Blog Exercise 3")
        except SpecialExercise.DoesNotExist:
            messages.error(request, 'You must complete this Exercise before you can proceed. Submit your result using internal CSS.')
            return redirect('blog_pg39')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@login_required(login_url="login")
def blog_ex3_submission(request):
    user=request.user
    try:
        has_submitted=SpecialExercise.objects.filter(user=request.user,title="Blog Exercise 3") #checks if a user has done the exercise
        if request.method == 'POST':
            if not has_submitted:
                    title=request.POST.get('title')
                    lang = request.POST.get('type')
                    code = request.POST.get('code')
                    special_exercise = SpecialExercise(user=user, title=title, type=lang, code=code, verified=False)
                    special_exercise.save()
                    return redirect('blog_ex3_SuccessView')
            else:
                return HttpResponse("You can't submitted thesame exercise twice.")
        else:
            return render(request, 'blog_ttrial/blog_ex3_submission.html', {'has_submitted':has_submitted})
        
    except:
        return HttpResponse("Something went wrong")
    
@login_required(login_url="login")    
def blog_ex3_SuccessView(request):
    return render(request, 'blog_ttrial/exercise3_success.html')



@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page40(request):
    code_1=BlogTTrial.objects.filter(title='blogP40_HTML1')

    context={
        'code_1':code_1,     
    }
    return render(request, 'blog_ttrial/page40.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page40_b(request):
    return render(request, 'blog_ttrial/page40_b.html')

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page41(request):
    code_1=BlogTTrial.objects.filter(title='blogP41_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP41_HTML1a')
    code_2=BlogTTrial.objects.filter(title='blogP41_CSS2')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,     
    }
    return render(request, 'blog_ttrial/page41.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page42(request):
    code_1=BlogTTrial.objects.filter(title='blogP42_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP42_HTML1a')
    code_2=BlogTTrial.objects.filter(title='blogP42_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP42_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,     
    }
    return render(request, 'blog_ttrial/page42.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page43(request):
    code_1=BlogTTrial.objects.filter(title='blogP43_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP43_HTML1a')
    code_2=BlogTTrial.objects.filter(title='blogP43_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP43_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,     
    }
    return render(request, 'blog_ttrial/page43.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page44(request):
    code_1=BlogTTrial.objects.filter(title='blogP44_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP44_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP44_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP44_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,     
    }
    return render(request, 'blog_ttrial/page44.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page45(request):
    code_1=BlogTTrial.objects.filter(title='blogP45_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP45_HTML1a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,     
    }
    return render(request, 'blog_ttrial/page45.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page46(request):
    code_1=BlogTTrial.objects.filter(title='blogP46_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP46_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP46_HTML2')
    code_2a=BlogTTrial.objects.filter(title='blogP46_HTML2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,     
    }
    return render(request, 'blog_ttrial/page46.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page47(request):
    code_1=BlogTTrial.objects.filter(title='blogP47_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP47_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP47_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP47_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,    
    }
    return render(request, 'blog_ttrial/page47.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page48(request):
    code_1=BlogTTrial.objects.filter(title='blogP48_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP48_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP48_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP48_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,     
    }
    return render(request, 'blog_ttrial/page48.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page49(request):
    code_1=BlogTTrial.objects.filter(title='blogP49_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP49_HTML1a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,     
    }
    return render(request, 'blog_ttrial/page49.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page50(request):
    code_1=BlogTTrial.objects.filter(title='blogP50_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP50_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP50_HTML2')
    code_2a=BlogTTrial.objects.filter(title='blogP50_HTML2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,    
    }
    return render(request, 'blog_ttrial/page50.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page51(request):
    code_1=BlogTTrial.objects.filter(title='blogP51_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP51_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP51_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP51_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,
        'code_2a':code_2a,     
    }
    return render(request, 'blog_ttrial/page51.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page52(request):
    code_1=BlogTTrial.objects.filter(title='blogP52_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP52_HTML1a')

    context={
        'code_1':code_1, 
        'code_1a':code_1a,  
    }
    return render(request, 'blog_ttrial/page52.html',context)


@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page53(request):
    code_1=BlogTTrial.objects.filter(title='blogP53_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP53_CSS1a')

    context={
        'code_1':code_1, 
        'code_1a':code_1a,   
    }
    return render(request, 'blog_ttrial/page53.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page54(request):
    code_1=BlogTTrial.objects.filter(title='blogP54_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP54_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP54_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP54_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,    
        'code_2a':code_2a, 
    }
    return render(request, 'blog_ttrial/page54.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page55(request):
    code_1=BlogTTrial.objects.filter(title='blogP55_HTML1')
    code_1a=BlogTTrial.objects.filter(title='blogP55_HTML1a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
           
    }
    return render(request, 'blog_ttrial/page55.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page56(request):
    code_1=BlogTTrial.objects.filter(title='blogP56_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP56_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP56_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP56_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,    
        'code_2a':code_2a,    
    }
    return render(request, 'blog_ttrial/page56.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page57(request):
    code_1=BlogTTrial.objects.filter(title='blogP57_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP57_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP57_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP57_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,    
        'code_2a':code_2a,     
    }
    return render(request, 'blog_ttrial/page57.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page58(request):
    code_1=BlogTTrial.objects.filter(title='blogP58_CSS1')
    code_1a=BlogTTrial.objects.filter(title='blogP58_CSS1a')
    code_2=BlogTTrial.objects.filter(title='blogP58_CSS2')
    code_2a=BlogTTrial.objects.filter(title='blogP58_CSS2a')

    context={
        'code_1':code_1,
        'code_1a':code_1a,
        'code_2':code_2,    
        'code_2a':code_2a,     
    }
    return render(request, 'blog_ttrial/page58.html',context)

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page59(request):
    has_submitted=SpecialExercise.objects.filter(user=request.user,title="Blog Exercise 4") #checks if a user has done the exercise
    return render(request, 'blog_ttrial/page59.html', {'has_submitted':has_submitted})

@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
def blogApp_page59_b(request):
    return render(request, 'blog_ttrial/page59_b.html')

#Excercise 4 logic
from functools import wraps

def require_special_exercise_submission_blog_ex4(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            SpecialExercise.objects.get(user=request.user,title="Blog Exercise 4")
        except SpecialExercise.DoesNotExist:
            messages.error(request, 'You must complete this Exercise before you can proceed. Submit your result using internal CSS.')
            return redirect('blog_pg59')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@login_required(login_url="login")
def blog_ex4_submission(request):
    user=request.user
    try:
        has_submitted=SpecialExercise.objects.filter(user=request.user,title="Blog Exercise 4") #checks if a user has done the exercise
        if request.method == 'POST':
            if not has_submitted:
                title=request.POST.get('title')
                lang = request.POST.get('type')
                code = request.POST.get('code')
                special_exercise = SpecialExercise(user=user, title=title, type=lang, code=code, verified=False)
                special_exercise.save()
                return redirect('blog_ex4_SuccessView')
            else:
                return HttpResponse("You can't submitted thesame exercise twice.")
        else:
            return render(request, 'blog_ttrial/blog_ex4_submission.html', {'has_submitted':has_submitted})
        
    except:
        return HttpResponse("Something went wrong")
    
@login_required(login_url="login")    
def blog_ex4_SuccessView(request):
    return render(request, 'blog_ttrial/exercise4_success.html')



@login_required(login_url="login")
@require_special_exercise_submission_HTML
@require_special_exercise_submission_CSS
@require_special_exercise_submission_blog_ex2
@require_special_exercise_submission_blog_ex3
@require_special_exercise_submission_blog_ex4
def blogApp_page60(request):
    return render(request, 'blog_ttrial/page60.html')





















# blog preview

def blogPreview_index(request):
    return render(request, 'blog_preview/index.html')

def blogPreview_trends(request):
    return render(request, 'blog_preview/trends.html')

def blogPreview_designers(request):
    return render(request, 'blog_preview/designers.html')

def blogPreview_outfits(request):
    return render(request, 'blog_preview/outfits.html')

def blogPreview_beauty(request):
    return render(request, 'blog_preview/beauty.html')

def blogPreview_about(request):
    return render(request, 'blog_preview/about.html')

def blogPreview_contact(request):
    return render(request, 'blog_preview/contact.html')

# break messages

def congrats(request):
    return render(request, 'break_messages/congrats.html')






    

