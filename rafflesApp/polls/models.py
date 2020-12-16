from django.db import models

# Create your models here.

class Question(models.Model):
    questionText = models.CharField(max_length=200)
    pubDate = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)