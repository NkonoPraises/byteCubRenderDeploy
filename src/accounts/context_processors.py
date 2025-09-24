from django.conf import settings

def base_url_processor(request):
    return {
        'BASE_URL':settings.BASE_URL
    }


#leaderboard context view
from quizApp.models import LeaderboardEntry

def leader_boards_context_view(request):
    rank=None
    points=None
    if request.user.is_authenticated:
        try:
            current_entry = LeaderboardEntry.objects.get(user=request.user)
            leaderboard = LeaderboardEntry.objects.filter(ranking_score=current_entry.ranking_score).order_by('-total_score')
            rank = LeaderboardEntry.objects.filter(
                ranking_score=current_entry.ranking_score,
                total_score__gt=current_entry.total_score
            ).count() + 1
            points=current_entry.total_score
        except LeaderboardEntry.DoesNotExist:
            rank = None  # or handle as needed
    return  {'rank':rank,'points':points}


