from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from accounts.forms import ExtendedUserCreationForm,AccountAuthenticationForm
from django.contrib import messages
from quizApp.models import LeaderboardEntry

def base_view(request):
    return render(request, 'base/index.html')

def mobile_appdev_landing(request):
    return render(request, 'base/react-native-landing.html')

def backend_webdev_landing(request):
    return render(request, 'base/backend-dev-landing.html')

def logout_view(request):
    logout(request)
    messages.success(request,"You are logged out")
    return redirect('base_view')
def register_view(request):
    
    # if request.user.is_anonymous:
    if request.method=='POST':
        form = ExtendedUserCreationForm(request.POST)
        # profile_form=UserProfileForm(request.POST)
        # if form.is_valid() and profile_form.is_valid():
        if form.is_valid():
            user=form.save()

            # profile=profile_form.save(commit=False)
            # profile.user=user
            # profile.save()

            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password1")
        
            
            user=authenticate(username=username,password=password)
            # if new_user is not None:
            login(request,user)
            messages.success(request,"You are welcome")
            return redirect('page3_view')

    else:
        # return redirect('home')
        form=ExtendedUserCreationForm()
        # profile_form=UserProfileForm()
    context={
        'form':form,
        #  'profile_form':profile_form
    }
    return render(request,'account/Sign-in.html',context)


def login_view(request):
    context={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You are logged in")
            return redirect('page3_view')

        else:
            messages.success(request,"There was an error logging in, Try again...")
            return redirect('login')
    else:
        return render(request,'account/login.html',context)
    



# Search functionality
from .models import SearchByteCub
from django.db.models import Q

def search_results(request):
    query = request.GET.get('query')
    if query:
        results = SearchByteCub.objects.filter(url_name__icontains=query).order_by('created_at')
    else:
        results = SearchByteCub.objects.all().order_by('created_at')

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search/search_results.html', context)

# Leader boards

def leader_boards_view(request):
    try:
        current_entry = LeaderboardEntry.objects.get(user=request.user)
        leaderboard = LeaderboardEntry.objects.filter(ranking_score=current_entry.ranking_score).order_by('-total_score')
        rank = LeaderboardEntry.objects.filter(
            ranking_score=current_entry.ranking_score,
            total_score__gt=current_entry.total_score
        ).count() + 1
    except LeaderboardEntry.DoesNotExist:
        rank = None  # or handle as needed
    return render(request, 'leaderboards/leader_boards.html', {'rank':rank,'leaderboard':leaderboard})

    