from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'
# those are the links fore core app 
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)