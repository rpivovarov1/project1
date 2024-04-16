from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import RegistrationForm


@login_required
def profile(request):
    print(request)
    user = request.user
    name = user.username
    email = user.email
    return render(request, 'profile.html', {'name': name, 'email': email})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            login(request, user)
            return redirect('/main/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def reg(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.get_user()
            login(request, user)
            return redirect('/main/')
    else:
        form = RegistrationForm()
    return render(request, 'reg.html', {'form': form})


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('http://127.0.0.1:8000/main/')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
