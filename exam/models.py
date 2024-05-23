from django.db import models
from rest_framework.exceptions import ValidationError
from user.models import User
from assets.models import Science

class Question(models.Model):
    science = models.ForeignKey(Science, on_delete=models.CASCADE)
    text = models.TextField()
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Savol'
        verbose_name_plural = 'Savollar'

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.question.text



class UserTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Test taken by {self.user} on {self.created_at}"

class UserTestQuestion(models.Model):
    user_test = models.ForeignKey(UserTest, related_name='questions', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"Question {self.question} in test {self.user_test}"

class UserTestAnswer(models.Model):
    user_test_question = models.OneToOneField(UserTestQuestion, on_delete=models.CASCADE, related_name='answer')
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Answer for {self.user_test_question}"

