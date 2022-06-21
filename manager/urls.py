
from django.contrib import admin
from django.urls import path
from django.urls import include

# links for all the project 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls', namespace='register')),
    path('project/', include('project.urls', namespace='project')),
    path('', include('core.urls', namespace='core')),
]