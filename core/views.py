from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponseRedirect
from register.models import Company
from register.models import Project
from register.models import UserProfile
from project.models import Task

# Create your views here.
# function for  home
def index(request):
    users = User.objects.all()
    users_prof = UserProfile.objects.all()
    if request.user.is_authenticated:
        try:
            logged_user = UserProfile.objects.get(user__username=request.user.username)
            context = {
                'users': users,
                'users_prof': users_prof,
                'logged_user': logged_user,
            }
            return render(request, 'core/index.html', context)
        except:
            users_prof = UserProfile.objects.all()
            context = {
                'users':users,
                'users_prof':users_prof,
            }
            return render(request, 'core/index.html', context)
    else:
        context = {
            'users': users,
            'users_prof': users_prof,
        }


    return render(request, 'core/index.html', context)

# function for dashboard
def dashboard(request):
    users = User.objects.all()
    active_users = User.objects.all().filter(is_active=True)
    companies = Company.objects.all()
    projects = Project.objects.all()
    tasks = Task.objects.all()
    context = {
        'users' : users,
        'active_users' : active_users,
        'companies' : companies,
        'projects' : projects,
        'tasks' : tasks,
    }
    return render(request, 'core/dashboard.html', context)


# function for login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)
            return redirect('core:index')
        else:
            return render(request, 'register/login.html', {'login_form':form})
    else:
        form = AuthenticationForm()
    return render(request, 'register/login.html', {'login_form':form})

# function for logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:index'))


   
    