from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from . import models
# from .forms import EmployeeFrom
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def base(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'registration.html')
