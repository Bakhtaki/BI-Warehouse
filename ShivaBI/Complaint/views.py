from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from .forms import LoginForm, UserRegisterForm
from . models import Complaint


def index(request):
    return render(request, 'Complaint/index.html')


# Register a new user
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    # Context
    context = {'form': form}
    return render(request, 'Complaint/register.html', context=context)


# Login a user
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            # Check if user exists
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'form': form}
    return render(request, 'Complaint/login.html', context=context)


# Dashboard the user
@login_required(login_url='login')
def dashboard(request):

    all_complaints = Complaint.objects.all()
    context = {'all_complaints': all_complaints}
    return render(request, 'Complaint/dashboard.html', context=context)


# Logout a user
def logout(request):
    auth.logout(request)
    return redirect('login')
