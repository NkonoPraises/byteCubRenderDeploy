from django.contrib import admin
from django.urls import path,include
from introToHTML_app.views import *

urlpatterns = [
    # path('index/',index_view,name="index"),
    path('HTMLIntro1/',page1_view,name="page1_view"),
    path('HTMLIntro2/',page2_view,name="page2_view"),
    path('HTMLIntro3/',page3_view,name="page3_view"),
    path('HTMLIntro_ex1/',HTMLIntro_ex1,name="HTMLIntro_ex1"),
    path('HTMLIntro4/',page4_view,name="page4_view"),
    path('HTMLIntro_ex2/',HTMLIntro_ex2,name="HTMLIntro_ex2"),
    path('HTMLIntro5/',page5_view,name="page5_view"),
    path('HTMLIntro5b/',page5b_view,name="page5b_view"),
    path('HTMLIntro_ex3/',HTMLIntro_ex3,name="HTMLIntro_ex3"),
    path('HTMLIntro6/',page6_view,name="page6_view"),
    path('HTMLIntro6b/',page6b_view,name="page6b_view"),
    path('HTMLIntro7/',page7_view,name="page7_view"),
    path('HTMLIntro7b/',page7b_view,name="page7b_view"),
    path('HTMLIntro_ex4/',HTMLIntro_ex4,name="HTMLIntro_ex4"),
    path('HTMLIntro8/',page8_view,name="page8_view"),
    path('HTMLIntro_ex5/',HTMLIntro_ex5,name="HTMLIntro_ex5"),
    path('HTMLIntro_ex5_submission/',Exercise5_submission, name="Exercise5_submission"),
    path('HTML_SuccessView/', HTML_SuccessView, name="HTML_SuccessView"),
]
