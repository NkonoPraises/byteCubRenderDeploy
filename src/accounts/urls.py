from django.urls import path
from accounts.views import register_view,logout_view,login_view,search_results,leader_boards_view,base_view,mobile_appdev_landing,backend_webdev_landing
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',register_view,name='register'),
    path('logout/',logout_view,name='logout'),
    path('login/',login_view,name='login'),



     # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),

    # base url
    path('',base_view, name="base_view" ),
    path('mobile_appdev/',mobile_appdev_landing, name="mobile_appdev_landing" ),
    path('backend_dev/',backend_webdev_landing, name="backend_webdev_landing" ),
    #  search functionality urls
    path('search/', search_results, name='search_results'),
    path('search-back/', search_results, name='home'),

    #leaderboard
    path('leader_board/', leader_boards_view, name='leader_board'),

]