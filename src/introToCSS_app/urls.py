from django.contrib import admin
from django.urls import path,include
from introToCSS_app.views import *

urlpatterns = [
    path('intro_to_css/', introduction_to_cssView, name="intro_to_css"),
    path('css_1/', CSS_intro_page1, name="css_1"),
    path('css_2/', CSS_intro_page2, name="css_2"),
    path('css_3/', CSS_intro_page3, name="css_3"),
    path('css_4/', CSS_intro_page4, name="css_4"),
    path('css_5/', CSS_intro_page5, name="css_5"),
    path('css_6/', CSS_intro_page6, name="css_6"),
    path('css_7/', CSS_intro_page7, name="css_7"),

    path('css_ex1/',CSSIntro_ex1, name="css_ex1"),
    path('css_ex2/',CSSIntro_ex2, name="css_ex2"),
    path('css_ex3/',CSSIntro_ex3, name="css_ex3"),

    path('CSSIntro_ex3_submission/',Exercise3_submission, name="Exercise3_submission"),
    path('CSS_SuccessView/', CSS_SuccessView, name="CSS_SuccessView")
    
]