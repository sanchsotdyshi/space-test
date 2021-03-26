from django.db import models

# Create your models here.

class Question(models.Model):
	task = models.CharField(max_length=150)
	first_option = models.CharField(max_length=70)
	second_option = models.CharField(max_length=70)
	third_option = models.CharField(max_length=70)
	fourth_option = models.CharField(max_length=70)
	correct_answer = models.IntegerField(default=0)
