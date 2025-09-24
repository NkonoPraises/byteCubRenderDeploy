from django import forms
from .models import UserSubscription

class ActivateSubscriptionForm(forms.Form):
    subscription_id = forms.UUIDField(
        label="Subscription ID",
        widget=forms.TextInput(attrs={
            'placeholder': 'Paste subscription ID here',
            'id': 'id_subscription_id'
        })
    )
    transaction_id = forms.CharField(
        max_length=100, 
        label="Transaction ID", 
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter transaction ID',
            'id': 'id_transaction_id'
        })
    )
    payment_method = forms.CharField(
        max_length=100, 
        label="Payment Method", 
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g., Bank Transfer, Mobile Money, etc.',
            'id': 'id_payment_method'
        })
    )