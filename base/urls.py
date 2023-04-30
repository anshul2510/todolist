from django.urls import path
from . import views 
from django.contrib.auth.views import (LoginView,
                                       LogoutView)

urlpatterns = [
    path('login/',views.CustomizeLoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(next_page= 'login'), name="logout"),
    path('register/',views.register,name='register'),
    path('create-task/',views.createtask,name='create-task'),
    path('update-task/<int:pk>/',views.updatetask,name='update-task'),
    path('delete-task/<int:pk>/',views.deletetask,name='delete-task'),
    path('taskdetails/<int:pk>/',views.taskdetails,name='taskdetails'),
    
    path('',views.home,name='home')
]