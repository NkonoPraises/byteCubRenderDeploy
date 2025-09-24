from django import forms
from .models import CodeSnippet1, Category1

class CodeSnippetForm(forms.ModelForm):
    class Meta:
        model = CodeSnippet1
        fields = ('title', 'code', 'language', 'category')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category1
        fields = ('name',)