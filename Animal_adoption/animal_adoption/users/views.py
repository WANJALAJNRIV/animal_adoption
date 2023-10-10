from .forms import UserForm, RegisterationForm, CustomAuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
from pets.models import Pet
from shelters.models import Shelter


def home(request):
    pets = Pet.objects.all().order_by('-last_updated')[:6]
    shelters = Shelter.objects.all()[:6]

    context = {
        'pets':pets,
        'shelters': shelters
    }

    return render(request, 'home.html', context)

def profile(request):
    return render(request, 'users/profile.html')


def register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()            
            login(request, user)
            return redirect('profile')  
    else:
        form = RegisterationForm()
    return render(request, 'auth/register.html', {'form': form})



# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'user':
                    return redirect('user_dashboard')
                elif user.role == 'manager':
                    return redirect('manager_dashboard')
                else:
                    return redirect('profile')  
    else:
        form = CustomAuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')  





from adoption_application.models import AdoptionApplication


def user_dashboard(request):
    application = AdoptionApplication.objects.filter(applicant=request.user)


    context = {
        'applications': application
    }


    return render(request, 'users/user_dashboard.html', context)

def manager_dashboard(request):

    return render(request, 'users/manager_dashboard.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/user_detail.html', {'user': user})


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()  
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})




