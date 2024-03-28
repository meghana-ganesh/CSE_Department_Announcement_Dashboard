from django.urls import path
from . import views
urlpatterns =[
    path('index/',views.index,name='index'),
    path('',views.login,name='login'),
    path('validateLogin/',views.validateLogin,name='validateLogin'),
    path('logout/',views.logout,name='logout'),
    
    ]
