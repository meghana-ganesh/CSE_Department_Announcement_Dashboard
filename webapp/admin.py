from django.contrib import admin
from .models import User,Announcements,Marks,Note

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','password','user']
    
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ['announcement','date']

class MarksAdmin(admin.ModelAdmin):
    list_display = ['test_name','student_regno','subject','marks','date']

class NotesAdmin(admin.ModelAdmin):
    list_display = ['title','document']

admin.site.register(User,UserAdmin)    
admin.site.register(Announcements,AnnouncementsAdmin)
admin.site.register(Marks,MarksAdmin)
admin.site.register(Note,NotesAdmin)