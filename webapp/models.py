from django.db import models

class User(models.Model):
    CHOICES = (('student','student'),('teacher','teacher'))
    username = models.IntegerField(primary_key = True)
    password = models.CharField(max_length = 100)
    user = models.CharField(max_length = 100,choices=CHOICES)


