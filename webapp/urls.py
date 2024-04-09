from django.urls import path
from . import views
urlpatterns =[
    path('index/',views.index,name='index'),
    path('',views.login,name='login'),
    path('validateLogin/',views.validateLogin,name='validateLogin'),
    path('logout/',views.logout,name='logout'),
    path('announcementsForm/',views.announcementsForm,name='announcementsForm'),
    path('addAnnouncements/',views.addAnnouncements,name='addAnnouncements'),
    path('deleteAnnouncement/<int:id>',views.deleteAnnouncement,name='deleteAnnouncement'),
    path('marksForm/',views.marksForm,name='marksForm'),
    path('addMarks/',views.addMarks,name='addMarks'),
    path('studentmarks_result/<str:subject>/',views.studentmarksResult,name='studentmarksResult'),
    path('teachermarks_result/<str:subject>/',views.teachermarksResult,name='teachermarksResult'),
    path('documentForm/',views.documentForm,name='documentForm'),
    path('addNotes/',views.addNotes,name='addNotes'),
    path('deleteNote/<int:id>/',views.deleteNote,name='deleteNote'),
    path('view-pdf/',views.pdf_view,name='pdf_view'),
    ]
