from django import forms
from .models import User,Announcements

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