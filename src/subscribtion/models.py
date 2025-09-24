from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from decimal import Decimal
import uuid

class SubscriptionPlan(models.Model):
    PLAN_CHOICES = [
        ('1_month', '1 Month Plan'),
        ('6_months', '6 Months Plan'),
        ('1_year', '1 Year Plan'),
    ]
    
    name = models.CharField(max_length=100)
    plan_type = models.CharField(max_length=20, choices=PLAN_CHOICES, unique=True)
    price_cfa = models.DecimalField(max_digits=10, decimal_places=2)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField(help_text="Duration in days")
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    # Add ordering for plan hierarchy (cheapest to most expensive)
    class Meta:
        ordering = ['price_usd']
    
    def str(self):
        return f"{self.name} - {self.get_plan_type_display()}"
    
    @property
    def price_rank(self):
        """Return the price rank to determine if a plan is an upgrade"""
        plans = list(SubscriptionPlan.objects.filter(is_active=True).order_by('price_usd'))
        return plans.index(self) + 1 if self in plans else 0
    
    @property
    def daily_rate_usd(self):
        return self.price_usd / Decimal(self.duration_days)
    
    @property
    def daily_rate_cfa(self):
        return self.price_cfa / Decimal(self.duration_days)
    

class UserSubscription(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Payment'),
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription')
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    subscription_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_upgrade = models.BooleanField(default=True)
    upgrade_price_usd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    upgrade_price_cfa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    previous_plan = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='upgraded_from')

    def is_active(self):
        if self.status != 'active':
            return False
        if self.end_date and timezone.now() > self.end_date:
            self.status = 'expired'
            self.save()
            return False
        return True
    
    def calculate_upgrade_price(self, new_plan):
        """Calculate prorated upgrade price"""
        if not self.is_active():
            return {
                'usd': new_plan.price_usd,
                'cfa': new_plan.price_cfa,
                'is_upgrade': False
            }
        
        # Calculate remaining days
        total_seconds = (self.end_date - self.start_date).total_seconds()
        remaining_seconds = (self.end_date - timezone.now()).total_seconds()
        remaining_days = max(1, int(remaining_seconds / 86400))  # At least 1 day
        
        # Calculate remaining value of current subscription
        remaining_value_usd = (self.plan.price_usd / Decimal(self.plan.duration_days)) * Decimal(remaining_days)
        remaining_value_cfa = (self.plan.price_cfa / Decimal(self.plan.duration_days)) * Decimal(remaining_days)
        
        # Calculate cost of new plan for full duration
        new_plan_value_usd = new_plan.price_usd
        new_plan_value_cfa = new_plan.price_cfa
        
        # Upgrade cost is the difference
        upgrade_cost_usd = max(Decimal('0'), new_plan_value_usd - remaining_value_usd)
        upgrade_cost_cfa = max(Decimal('0'), new_plan_value_cfa - remaining_value_cfa)
        
        return {
            'usd': upgrade_cost_usd,
            'cfa': upgrade_cost_cfa,
            'remaining_days': remaining_days,
            'is_upgrade': True
        }
    
    def str(self):
        return f"{self.user.email} - {self.plan.name if self.plan else 'No Plan'} - {self.status}"