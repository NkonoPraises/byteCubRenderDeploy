from django.urls import path
from .views import *

app_name = 'exerciseApp'
urlpatterns = [
    path('exercise_list/',exercise_list, name="exercise_list"),
    # path('test/',test, name="test"),
    path('ex/<str:exercise_name>/',exercise_detail, name='exercise_detail'), #Load everything by name
    path('submission/<str:exercise_name>/', submission_detail, name='submission_detail'),

    #admin review urls
    path('review_list/', exercises_list, name='exercises_list'),
    path('exercise/<str:exercise_title>/', exercise_submissions, name='exercise_submissions'),
    path('submissions/<int:submission_id>/', submission_details, name='submission_details'),
    path('submit-review/<int:submission_id>/', submit_review, name='submit_review'),

    #user reviews url
    path('my-reviews/',user_reviews, name='user_reviews'),
]