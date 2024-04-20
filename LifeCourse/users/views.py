from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse


from .forms import UserLoginForm, UserRegisterForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, '', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, '', context=context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.POST, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {'title': 'Личный кабинет', 'form': form}
    return render(request, 'user/profile.html', context=context)


def login(request):
    return render(request, '')


def register(request):
    return render(request, '')
