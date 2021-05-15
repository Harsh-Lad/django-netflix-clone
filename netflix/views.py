from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from netflix.forms import UserAdminCreationForm
from .models import CustomUser as User
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request,'authentication/index.html')

def login(request):
    if request.user.is_authenticated: 
        return redirect('browse')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            
            user = auth.authenticate(username= email, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("browse")
                            
            else:
                return redirect('login')
        else:
            return render(request,'authentication/login.html')

def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'authentication/register.html')

def browse(request):
    username = request.user.username
    return render(request,'userDash/browse.html',{'userEmail':username})

def latest(request):
    return render(request,'userDash/latest.html')

def tvshow(request):
    return render(request,'userDash/tvshow.html')

def movies(request):
    return render(request,'userDash/movies.html')

def mylist(request):
    return render(request,'userDash/mylist.html')

def search(request):
    return render(request,'userDash/search.html')

def single(request):
    return render(request,'userDash/single.html')