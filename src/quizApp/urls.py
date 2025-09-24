from django.urls import path
# from .views import quiz_page, quiz_answer,profile_view,code_quiz_answer,code_quiz
from .views import *

app_name = 'quizApp'

urlpatterns = [
    # path('quiz/', quiz_page, name='quiz_page'),
    # path('answer/<int:question_id>/', quiz_answer, name='quiz_answer'),
    # path('answer/', quiz_answer, name='quiz_answer'),
    # path('profile/', profile_view, name='profile'),
    # path('code_quiz/', code_quiz, name='code_quiz'),
    # path('code_quiz_answer/', code_quiz_answer, name='code_quiz_answer'),

    path('base/', base_view, name='base_view'),

    path('<str:quiz_name>/', quiz_page, name='quiz_page'),
    path('<str:quiz_name>/submit/', submit_quiz, name='submit_quiz'),
    path('<str:quiz_name>/answer/', answer_page, name='answer_page'),
]