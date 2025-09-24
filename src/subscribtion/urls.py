from django.urls import path
from .views import *



urlpatterns = [
    # path('subscription/', subscription_status, name='subscription_status'),
    # path('subscription/choose-plan/<int:plan_id>/', choose_plan, name='choose_plan'),
    # path('subscription/payment/<int:plan_id>/', payment_page, name='payment'),
    # path('subscription/payment-success/<int:plan_id>/', payment_success, name='payment_success'),
    # path('subscription/payment-cancel/', payment_cancel, name='payment_cancel'),

    # URL for the protected view
    path('plans/', subscription_plans, name='plans'),
    path('choose-plan/<int:plan_id>/', choose_plan, name='choose_plan'),
     path('calculate-upgrade/<int:current_plan_id>/<int:new_plan_id>/',calculate_upgrade_price, name='calculate_upgrade'),
    path('my-subscription/', my_subscription, name='my_subscription'),
    path('activation/', subscription_activation, name='activation'),
    path('premium-content/', premium_content, name='premium_content'),
]