from django.shortcuts import render, redirect
from .models import CodeSnippet1, Category1
from .forms import CodeSnippetForm, CategoryForm

def code_editor_view(request):
    if request.method == 'POST':
        if 'snippet' in request.POST:
            form = CodeSnippetForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        elif 'category' in request.POST:
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
    else:
        form = CodeSnippetForm()
        category_form = CategoryForm()

    categories = Category1.objects.all()
    snippets = CodeSnippet1.objects.all()
    return render(request, 'code_editor/editor.html', {'form': form, 'category_form': category_form, 'categories': categories, 'snippets': snippets})


def index(request):
    snippets=CodeSnippet1.objects.filter(title='code y')
    return render(request, 'code_editor/page1.html',{'snippets':snippets})

def page_1(request):
    snippets=CodeSnippet1.objects.filter(title='code y')
    return render(request, 'code_editor/page1.html',{'snippets':snippets})
