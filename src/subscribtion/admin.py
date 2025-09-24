from django.contrib import admin
from .models import SubscriptionPlan, UserSubscription

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'plan_type', 'price_cfa', 'price_usd', 'duration_days', 'is_active']
    list_filter = ['plan_type', 'is_active']
    list_editable = ['price_cfa', 'price_usd', 'is_active']

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'status', 'start_date', 'end_date', 'payment_method']
    list_filter = ['status', 'plan']
    search_fields = ['userusername', 'useremail', 'subscription_id']
    readonly_fields = ['subscription_id', 'created_at', 'updated_at']