from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Exercise)
admin.site.register(CodeSubmission)
admin.site.register(CompletedExercise)
admin.site.register(SpecialExercise)
admin.site.register(ExerciseRemarks)
