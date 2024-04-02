from django.db import models

class User(models.Model):
    CHOICES = (('student','student'),('teacher','teacher'))
    username = models.IntegerField(primary_key = True)
    password = models.CharField(max_length = 100)
    user = models.CharField(max_length = 100,choices=CHOICES)
class Announcements(models.Model):
    announcement = models.CharField(max_length=500)
    date = models.DateField()
class Marks(models.Model):
    test_name = models.CharField(max_length=100)
    student_regno = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.PositiveIntegerField(default = 0)
    date = models.DateField()
class Note(models.Model):
    title = models.CharField(max_length=100)
    document = models.FileField(upload_to='notes/')
    date = models.DateField()