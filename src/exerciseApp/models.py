from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone

class Exercise(models.Model):
    exercise_name = models.CharField(max_length=255, unique=True,
                                 validators=[RegexValidator(regex='^[a-zA-Z0-9_-]+$',
                                                            message='Only alphanumeric characters, underscores, and hyphens are allowed.')], blank=True, null=True) #Load by exercise name
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)  #Detailed instructions for the exercise
    reference_code = models.TextField()  # 

    def __str__(self):
        return self.title

class CodeSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    code = models.TextField()
    submission_time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0) #Score for the submission

    def __str__(self):
        return f"Submission by {self.user.username} for {self.exercise.title}"
    
class CompletedExercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    completed_time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.exercise.title} - {self.score}"
    
class SpecialExercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=90)
    type=models.CharField(max_length=90)
    code = models.TextField()
    verified = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "SpecialExercises"

    def __str__(self):
        return self.title
    
class ExerciseRemarks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_title = models.CharField(max_length=200)
    remarks = models.TextField()
    score = models.IntegerField()
    code = models.TextField(default="console.log('Your code')")
    date = models.DateTimeField(default=timezone.now)
    
    def status(self):
        if self.score >= 70:
            return "passed"
        elif self.score >= 50:
            return "fair"
        return "failed"

    def __str__(self):
        return f"Feedback for {self.exercise_title} by {self.user.username}"