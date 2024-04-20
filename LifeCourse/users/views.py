from django.shortcuts import render

from .models import User
from .forms import UserLoginForm


def login(request):
    context = {'form': UserLoginForm()}
    return render(request, '', context=context)


def register(request):
    return render(request, '')
