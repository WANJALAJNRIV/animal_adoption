from .forms import (
    UserForm,
    RegisterationForm,
    CustomAuthenticationForm,
)
from django.contrib.auth import (
    login,
    logout,
    authenticate,
)
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from .models import User
from pets.models import Pet
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from adoption_application.models import AdoptionApplication
from django.http import HttpResponseForbidden
from .decorators import user_required, admin_required


def home(request):
    """
    Render the home page with a list of pets and shelters.

    Retrieves the latest 6 pets and the first 6 shelters to display on the home page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered home page with context data.
    """
    pets = Pet.objects.filter(adoption_status='Available').order_by('-last_updated')[:6]

    return render(request, 'home.html',{ 'pets':pets})


@login_required
def profile(request):
    """
    Render the user's profile page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered user profile page.
    """
    return render(request, 'users/profile.html')


def register(request):
    """
    Register a new user.

    This view allows users to register a new account. If the request method is POST,
    it processes the registration form, creates a new user, and logs them in.
    If the request method is GET, it displays the registration form.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML template or a redirect response.
    :rtype: HttpResponse
    """

    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()            
            login(request, user)
            messages.success(request, 'You have been successfully registered.')
            return redirect('profile')  
    else:
        form = RegisterationForm()
    return render(request, 'auth/register.html', {'form': form})


def user_login(request):
    """
    Log in a user.

    This view handles user login. If the request method is POST, it processes the login form,
    authenticates the user, and logs them in. Depending on the user's role (e.g., 'user', 'manager'),
    it redirects them to the appropriate dashboard.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML template or a redirect response.
    :rtype: HttpResponse
    """


    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    if user.role == 'user':
                        messages.success(request, 'You have successfully logged in.')
                        return redirect('user_dashboard')
                    elif user.role == 'admin' or user.role == 'application_manager'  or user.role == 'pet_manager' :
                        messages.success(request, 'You have successfully logged in.')
                        return redirect('staff_dashboard')
                    else:
                        messages.success(request, 'You have successfully logged in.')
                        return redirect('profile')  
    else:
        form = CustomAuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


@login_required
def user_logout(request):
    """
    Log out a user.

    This view logs out the currently authenticated user and redirects them to the login page.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A redirect response to the login page.
    :rtype: HttpResponse
    """

    logout(request)
    messages.success(request, 'Logout is successful.Please login to continue')
    return redirect('home')  


@login_required
@user_required
def user_dashboard(request):
    """
    Display the user dashboard.

    This view displays the dashboard for authenticated users, showing their adoption applications.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML template with the user's adoption applications.
    :rtype: HttpResponse
    """

    application = AdoptionApplication.objects.filter(applicant=request.user).order_by('-last_updated')
    return render(request, 'users/user_dashboard.html', {'applications': application})


@login_required
def staff_dashboard(request):
    """
    Display the staff dashboard.

    This view displays the staff dashboard and is protected with the login_required decorator.
    
    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML template.
    :rtype: HttpResponse
    """
    return render(request, 'users/staff_dashboard.html')


@login_required
@admin_required
def user_list(request):
    """
    Display a list of users.

    This view displays a list of users and is protected with the login_required and admin_required decorators.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML template with a list of users.
    :rtype: HttpResponse
    """

    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


@login_required
@admin_required
def user_detail(request, user_id):
    """
    Display details of a user.

    This view displays the details of a specific user and is protected with the login_required and admin_required decorators.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param user_id: The ID of the user to display.
    :type user_id: int
    :return: A rendered HTML template with the user's details.
    :rtype: HttpResponse
    """
  
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/user_detail.html', {'user': user})


@login_required
@admin_required
def user_create(request):
    """
    Create a new user.

    This view allows administrators to create new user accounts. It is protected with the login_required and admin_required decorators.
    If the request method is POST, it processes the user creation form and saves the new user. 
    If the request method is GET, it displays the user creation form.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML template or a redirect response.
    :rtype: HttpResponse
    """

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save() 
            messages.success(request, 'User has been created successfully.')
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})


@login_required
@admin_required
def user_update(request, pk):
    """
    Update an existing user.

    This view allows administrators to update the information of an existing user account.
    It is protected with the login_required and admin_required decorators.
    If the request method is POST, it processes the user update form and saves the changes.
    If the request method is GET, it displays the user update form with the user's current information.

    :param request: The HTTP request object.
    :param pk: The primary key of the user to be updated.
    :type request: HttpRequest
    :type pk: int
    :return: A rendered HTML template or a redirect response.
    :rtype: HttpResponse
    """
 
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            messages.success(request, 'User has been updated successfully.')
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})


@login_required
@admin_required
def user_delete(request, pk):
    """
    Delete an existing user.

    This view allows administrators to delete an existing user account.
    It is protected with the login_required and admin_required decorators.
    If the request method is POST, it deletes the user account.
    If the request method is GET, it displays a confirmation page before deleting the user.

    :param request: The HTTP request object.
    :param pk: The primary key of the user to be deleted.
    :type request: HttpRequest
    :type pk: int
    :return: A rendered HTML template or a redirect response.
    :rtype: HttpResponse
    """
 
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User has been deleted successfully.')
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})




