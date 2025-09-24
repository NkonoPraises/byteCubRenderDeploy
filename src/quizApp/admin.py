# from django.contrib import admin
# from .models import Quiz, Question, Choice, QuizSubmission, Answer, LeaderboardEntry

# admin.site.register(Quiz)
# admin.site.register(Question)
# admin.site.register(Choice)
# admin.site.register(QuizSubmission)
# admin.site.register(Answer)
# admin.site.register(LeaderboardEntry)

from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(Quiz)
admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(QuizSubmission)
admin.site.register(Answer)
admin.site.register(LeaderboardEntry)
admin.site.register(ImageUpload)
