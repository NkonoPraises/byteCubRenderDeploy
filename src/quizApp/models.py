from django.db import models
from django.contrib.auth.models import User



# from django.db import models
# from django.contrib.auth.models import User

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=9999, unique=True)  # Unique for each quiz
    title = models.CharField(max_length=9999)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=255, default="link")

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField(max_length=99999)
    option_a = models.CharField(max_length=9999, blank=True, null=True )
    option_b = models.CharField(max_length=9999, blank=True, null=True )
    option_c = models.CharField(max_length=9999, blank=True, null=True )
    option_d = models.CharField(max_length=9999, blank=True, null=True )
    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ('A', 'Option A'),
            ('B', 'Option B'),
            ('C', 'Option C'),
            ('D', 'Option D'),
        ],
        blank=True,
        null=True
    )
    explanation = models.TextField(blank=True) 

    def __str__(self):
        return self.text

# class Choice(models.Model):
#     question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
#     text = models.CharField(max_length=255)
#     is_correct = models.BooleanField(default=False)

#     def __str__(self):
#         return self.text

class QuizSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    submission_time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - {self.score}"

class Answer(models.Model):
    submission = models.ForeignKey(QuizSubmission, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # chosen_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)  # User's choice
    chosen_answer = models.CharField(
        max_length=1,
        choices=[
            ('A', 'Option A'),
            ('B', 'Option B'),
            ('C', 'Option C'),
            ('D', 'Option D'),
            (None, 'Unanswered'),  # Use None for unanswered
        ],
        blank=True,
        null=True,  # Allow null values for unanswered questions
    )
    
    def __str__(self):
        return f"Answer to {self.question.text} by {self.submission.user.username}"

    class Meta:
        unique_together = ('submission', 'question') #one answer per question

class LeaderboardEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.IntegerField()
    ranking_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.total_score} points"
    

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded at {self.uploaded_at}"
