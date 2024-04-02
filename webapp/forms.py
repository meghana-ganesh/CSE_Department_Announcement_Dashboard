from django import forms
from .models import User,Announcements,Marks,Note

class LoginForm(forms.ModelForm): 
    class Meta:
        model = User
        fields = ['username','password','user']
class AnnouncementsForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ['announcement','date']
        widgets = {
            'date': forms.SelectDateWidget()
        }
class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['test_name','student_regno','subject','marks','date']
        widgets = {
            'date' : forms.SelectDateWidget()
            }
class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title','document','date']
        widgets = {
            'date' : forms.SelectDateWidget()
            }
