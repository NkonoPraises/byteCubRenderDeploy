from django import forms
from .models import Answer

class CodeSubmissionForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['submitted_code'] # Just the code field for submission
        widgets = {
            'submitted_code': forms.Textarea(attrs={'class': 'code-editor',
                                                     'placeholder': 'Paste your code here...'}),
        }