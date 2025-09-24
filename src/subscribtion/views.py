from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q
from .models import SubscriptionPlan, UserSubscription
from .forms import ActivateSubscriptionForm
import urllib.parse
from django.http import HttpResponse
from .decorators import *

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from .models import SubscriptionPlan, UserSubscription
from .forms import ActivateSubscriptionForm
import urllib.parse
from decimal import Decimal

@login_required
def subscription_plans(request):
    plans = SubscriptionPlan.objects.filter(is_active=True).order_by('price_usd')
    
    # Get user's current active or pending subscription
    user_subscription = UserSubscription.objects.filter(
        user=request.user
    ).exclude(status='expired').exclude(status='cancelled').first()
    
    # Calculate upgrade prices for each plan
    upgrade_info = {}
    if user_subscription and user_subscription.is_active():
        for plan in plans:
            if plan.price_usd > user_subscription.plan.price_usd:
                upgrade_info[plan.id] = user_subscription.calculate_upgrade_price(plan)
    
    context = {
        'plans': plans,
        'user_email': request.user.email,
        'user_subscription': user_subscription,
        'upgrade_info': upgrade_info
    }
    return render(request, 'subscription/plans.html', context)

@login_required
def calculate_upgrade_price(request, current_plan_id, new_plan_id):
    """API endpoint to calculate upgrade price"""
    try:
        current_sub = UserSubscription.objects.get(
            id=current_plan_id,
            user=request.user,
            status='active'
        )
        new_plan = SubscriptionPlan.objects.get(id=new_plan_id, is_active=True)
        
        if new_plan.price_usd <= current_sub.plan.price_usd:
            return JsonResponse({'error': 'Can only upgrade to higher-tier plans'})
        
        upgrade_data = current_sub.calculate_upgrade_price(new_plan)
        
        return JsonResponse({
            'upgrade_price_usd': float(upgrade_data['usd']),
            'upgrade_price_cfa': float(upgrade_data['cfa']),
            'remaining_days': upgrade_data['remaining_days'],
            'is_upgrade': upgrade_data['is_upgrade']
        })
        
    except (UserSubscription.DoesNotExist, SubscriptionPlan.DoesNotExist):
        return JsonResponse({'error': 'Invalid plan or subscription'})

@login_required
def choose_plan(request, plan_id):
    plan = get_object_or_404(SubscriptionPlan, id=plan_id, is_active=True)
    
    # Check if user already has this plan pending or active
    existing_subscription = UserSubscription.objects.filter(
        user=request.user,
        plan=plan
    ).exclude(status='expired').exclude(status='cancelled').first()
    
    if existing_subscription:
        if existing_subscription.status == 'pending':
            messages.warning(request, f"You already have a pending subscription for {plan.name}. Please complete the payment first.")
            return redirect('my_subscription')
        elif existing_subscription.status == 'active':
            messages.warning(request, f"You already have an active {plan.name} subscription.")
            return redirect('my_subscription')
    
    # Check if user has an active subscription
    active_subscription = UserSubscription.objects.filter(
        user=request.user,
        status='active'
    ).first()
    
    is_upgrade = False
    upgrade_price_usd = Decimal('0')
    upgrade_price_cfa = Decimal('0')
    
    if active_subscription and active_subscription.is_active():
        if active_subscription.plan == plan:
            messages.warning(request, "You already have this plan active.")
            return redirect('plans')
        
        # Check if this is an upgrade
        if plan.price_usd > active_subscription.plan.price_usd:
            is_upgrade = True
            upgrade_data = active_subscription.calculate_upgrade_price(plan)
            upgrade_price_usd = upgrade_data['usd']
            upgrade_price_cfa = upgrade_data['cfa']
        else:
            messages.warning(request, "You can only upgrade to a higher-tier plan.")
            return redirect('plans')
    
    # Create a new subscription (pending)
    subscription = UserSubscription.objects.create(
        user=request.user,
        plan=plan,
        status='pending',
        is_upgrade=is_upgrade,
        upgrade_price_usd=upgrade_price_usd if is_upgrade else None,
        upgrade_price_cfa=upgrade_price_cfa if is_upgrade else None
    )
    
    if is_upgrade:
        subscription.previous_plan = active_subscription
        subscription.save()
    
    # Prepare WhatsApp message
    whatsapp_number = "+237695221180"  # Replace with your number
    
    if is_upgrade:
        message = (
            f"Hello! I want to UPGRADE my subscription:\n"
            f"• From: {active_subscription.plan.name} (${active_subscription.plan.price_usd})\n"
            f"• To: {plan.name} (${plan.price_usd})\n"
            f"• Upgrade cost: ${upgrade_price_usd:.2f} USD / {upgrade_price_cfa:.0f} CFA Frs\n"
            f"• My email: {request.user.email}"
        )
    else:
        message = (
            f"Hello! I want to subscribe to:\n"
            f"• Plan: {plan.name}\n"
            f"• Price: ${plan.price_usd} USD / {plan.price_cfa} CFA Frs\n"
            f"• Duration: {plan.duration_days} days\n"
            f"• My email: {request.user.email}"
        )
    
    encoded_message = urllib.parse.quote(message)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_message}"
    
    if is_upgrade:
        messages.success(request, f"Upgrade requested! You'll pay only ${upgrade_price_usd:.2f} for the remaining period.")
    else:
        messages.success(request, f"You've selected the {plan.name} plan.")
    
    return redirect(whatsapp_url)

@login_required
def my_subscription(request):
    subscriptions = UserSubscription.objects.filter(user=request.user).order_by('-created_at')
    active_subscription = subscriptions.filter(status='active').first()
    pending_subscription = subscriptions.filter(status='pending').first()
    
    # Get available upgrades
    available_upgrades = []
    if active_subscription and active_subscription.is_active():
        available_upgrades = SubscriptionPlan.objects.filter(
            is_active=True,
            price_usd__gt=active_subscription.plan.price_usd
        )
    
    context = {
        'subscriptions': subscriptions,
        'active_subscription': active_subscription,
        'pending_subscription': pending_subscription,
        'available_upgrades': available_upgrades
    }
    return render(request, 'subscription/my_subscription.html', context)

# Admin views for activation
def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def subscription_activation(request):
    search_query = request.GET.get('search', '')
    
    # Base querysets
    pending_subscriptions = UserSubscription.objects.filter(status='pending').order_by('-created_at')
    active_subscriptions = UserSubscription.objects.filter(status='active').order_by('-end_date')
    
    # Apply search filter if query exists
    if search_query:
        pending_subscriptions = pending_subscriptions.filter(
            Q(useremailicontains=search_query) |
            Q(subscription_id__icontains=search_query) |
            Q(plannameicontains=search_query)
        )
        active_subscriptions = active_subscriptions.filter(
            Q(useremailicontains=search_query) |
            Q(subscription_id__icontains=search_query) |
            Q(plannameicontains=search_query) |
            Q(transaction_id__icontains=search_query)
        )
    
    if request.method == 'POST':
        form = ActivateSubscriptionForm(request.POST)
        if form.is_valid():
            subscription_id = form.cleaned_data['subscription_id']
            transaction_id = form.cleaned_data['transaction_id']
            payment_method = form.cleaned_data['payment_method']
            
            try:
                subscription = UserSubscription.objects.get(
                    subscription_id=subscription_id, 
                    status='pending'
                )
                
                # If this is an upgrade, handle the previous subscription
                if subscription.is_upgrade and subscription.previous_plan:
                    previous_sub = subscription.previous_plan
                    previous_sub.status = 'cancelled'
                    previous_sub.save()
                
                # Calculate end date based on plan duration
                start_date = timezone.now()
                end_date = start_date + timezone.timedelta(days=subscription.plan.duration_days)
                
                subscription.status = 'active'
                subscription.start_date = start_date
                subscription.end_date = end_date
                subscription.transaction_id = transaction_id
                subscription.payment_method = payment_method
                subscription.save()
                
                messages.success(request, f"Subscription activated for {subscription.user.email}")
                
            except UserSubscription.DoesNotExist:
                messages.error(request, "Subscription not found or already activated")
            
            return redirect('activation')
    else:
        form = ActivateSubscriptionForm()
    
    context = {
        'pending_subscriptions': pending_subscriptions,
        'active_subscriptions': active_subscriptions,
        'form': form,
        'search_query': search_query
    }
    return render(request, 'subscription/activation.html', context)

# Protected view example
@login_required
@subscription_required
def premium_content(request):
    return HttpResponse("Premuim page")

