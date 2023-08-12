from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from .forms import (
    LoginForm, UserRegisterForm,
    CreateComplaintForm, UpdateComplaintForm
)
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

    complaints = Complaint.objects.all()
    context = {'complaints': complaints}
    return render(request, 'Complaint/dashboard.html', context=context)


# Create the new Complaint
@login_required(login_url='login')
def create_complaint(request):
    form = CreateComplaintForm()
    if request.method == 'POST':
        form = CreateComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'Complaint/create_complaint.html', context=context)


# Update the Complaint
@login_required(login_url='login')
def update_complaint(request, pk):
    complaint = Complaint.objects.get(id=pk)
    form = UpdateComplaintForm(instance=complaint)

    if request.method == 'POST':
        form = UpdateComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'Complaint/update_complaint.html', context=context)


# View the single Complaint
@login_required(login_url='login')
def view_complaint(request, pk):

    # All Complaints
    all_complaints = Complaint.objects.get(id=pk)
    context = {'complaint': all_complaints}

    return render(request, 'Complaint/view_complaint.html', context=context)



# Logout a user
def logout(request):
    auth.logout(request)
    return redirect('login')
