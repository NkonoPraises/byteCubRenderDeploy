from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps
from .models import UserSubscription

def subscription_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        # Check if user has an active subscription
        active_subscription = UserSubscription.objects.filter(
            user=request.user, 
            status='active'
        ).first()
        
        if not active_subscription or not active_subscription.is_active():
            return redirect('plans')
        
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view

def combined_auth_required(view_func):
    @login_required
    @subscription_required
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view