from django.urls import path
from . import views

app_name = 'register'
# those are the links for register app 
urlpatterns = [
    path('new-user/', views.register, name='new-user'),
    path('new-company/', views.newCompany, name='new-company'),
    path('users/', views.usersView, name='users'),
    path('users/profile', views.profile, name='profile'),
    path('users/', views.user_view, name='user'),
]

