from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from .forms import LoginForm, UserRegisterForm


def index(request):
    return render(request, 'Complaint/index.html')


# Register a new user
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('Complaint:login')
    # Context
    context = {'form': form}
    return render(request, 'Complaint/register.html', context=context)
