from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib import messages

# Registration view
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            messages.error(request, "Error in registration")
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')

# Profile view
def profile(request):
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, "Profile updated successfully!")
    return render(request, 'blog/profile.html')
