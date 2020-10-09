from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm
from django.contrib import messages





def signup_view(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            return redirect('app:inicio')
            
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

  
       

    

    
 
 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('app:inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
 
 
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('app:inicio')



