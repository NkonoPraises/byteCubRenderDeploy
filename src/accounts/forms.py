# from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate
# from userprofile.models import UserProfile

# class RegistrationForm(UserCreationForm):
#     email   =forms.EmailField(max_length=60,help_text="user must add a valid email address")

#     class Meta:
#         model=User
#         fields=['email','username','password1','password2']

class ExtendedUserCreationForm(UserCreationForm):
    email=forms.EmailField(label="",widget=forms.EmailInput(attrs={'class':'style','placeholder':'Email:'}),required=True)
    username=forms.CharField(max_length=150,label="",widget=forms.TextInput(attrs={'class':'style','placeholder':'Username:'}),required=True)
    first_name=forms.CharField(max_length=150,label="",widget=forms.TextInput(attrs={'class':'style','placeholder':'First name:'}),required=True)
    last_name=forms.CharField(max_length=150,label="",widget=forms.TextInput(attrs={'class':'style','placeholder':'Last name:'}),required=True)
    password1=forms.CharField(max_length=150,label="",widget=forms.PasswordInput(attrs={'class':'style','placeholder':'Password:'}),required=True)
    password2=forms.CharField(max_length=150,label="",widget=forms.PasswordInput(attrs={'class':'style','placeholder':'Confrim password:'}),required=True)

    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password1','password2')

    def save(self, commit=True):
        user=super().save(commit=False)

        user.email=self.cleaned_data['email']
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['email','password']

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email,password=password):
                raise forms.ValidationError("invalid login")

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model=UserProfile
#         fields=['title',]