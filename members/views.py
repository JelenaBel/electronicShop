from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib import sessions


# login user functionality (checking is it correct user and correct password in the database)
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('main')

        else:
            messages.success(request, 'There was an error in login, Try Again')
            return redirect('login')
    # Return an 'invalid login' error message.
    else:
        return render(request, 'authenticate/login.html', {})


# logout user functionality
def logout_user(request):
    logout(request)
    messages.success(request, 'You are successfully logout')
    return redirect('main')


# register user functionality and adding User info to the database
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You are successfully register.')
            return redirect('main')

    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {
            'form': form,
            })
