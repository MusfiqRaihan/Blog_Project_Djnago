from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUser


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

            else:
                messages.add_message(request, messages.ERROR, 'Username Or Password Mismatch!')

    return render(request, 'user/login.html')


def user_register(request):
    form = RegisterUser(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Registration Successfully Completed")
        return redirect('login')
    return render(request, 'user/register.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('/')
