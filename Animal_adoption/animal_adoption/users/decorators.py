from functools import wraps
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse


def user_required(function):
    """
    Decorator for views that require the user's role to be 'user'.

    If the user's role is 'user', the view is executed. Otherwise, a 'Permission denied' message is displayed, and the user is redirected to the previous page they were on. If there's no previous page, an 'Permission denied' message is displayed.

    :param function: The view function to decorate.
    :type function: callable
    :return: The wrapped view function.
    :rtype: callable
    """

    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if request.user.role == 'user':
            return function(request, *args, **kwargs)
        else:
            messages.error(request, 'Permission denied.')
            previous_url = request.META.get('HTTP_REFERER')
            if previous_url:
                return HttpResponseRedirect(previous_url)
            else:
                # Handle the case where there's no previous URL
                return HttpResponse("Permission denied")
    return wrapper


def admin_required(function):
    """
    Decorator for views that require the user's role to be 'admin'.

    If the user's role is 'admin', the view is executed. Otherwise, a 'Permission denied' message is displayed, and the user is redirected to the previous page they were on. If there's no previous page, an 'Permission denied' message is displayed.

    :param function: The view function to decorate.
    :type function: callable
    :return: The wrapped view function.
    :rtype: callable
    """

    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if request.user.role == 'admin':
            return function(request, *args, **kwargs)
        else:
            messages.error(request, 'Permission denied.')
            previous_url = request.META.get('HTTP_REFERER')
            if previous_url:
                return HttpResponseRedirect(previous_url)
            else:
                # Handle the case where there's no previous URL
                return HttpResponse("Permission denied")
    return wrapper

def application_manager_or_admin_required(view_func):
    """
    Decorator for views that require the user's role to be 'application_manager' or 'admin'.

    If the user's role is 'application_manager' or 'admin', the view is executed. Otherwise, a 'Permission denied' message is displayed, and the user is redirected to the previous page they were on. If there's no previous page, an 'Permission denied' message is displayed.

    :param view_func: The view function to decorate.
    :type view_func: callable
    :return: The wrapped view function.
    :rtype: callable
    """

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role in ['application_manager', 'admin']:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'Permission denied.')
            previous_url = request.META.get('HTTP_REFERER')
            if previous_url:
                return HttpResponseRedirect(previous_url)
            else:
                # Handle the case where there's no previous URL
                return HttpResponse("Permission denied")
    return wrapper


def pet_manager_or_admin_required(view_func):
    """
    Decorator for views that require the user's role to be 'pet_manager' or 'admin'.

    If the user's role is 'pet_manager' or 'admin', the view is executed. Otherwise, a 'Permission denied' message is displayed, and the user is redirected to the previous page they were on. If there's no previous page, an 'Permission denied' message is displayed.

    :param view_func: The view function to decorate.
    :type view_func: callable
    :return: The wrapped view function.
    :rtype: callable
    """
    
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role in ['pet_manager', 'admin']:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'Permission denied.')
            previous_url = request.META.get('HTTP_REFERER')
            if previous_url:
                return HttpResponseRedirect(previous_url)
            else:
                # Handle the case where there's no previous URL
                return HttpResponse("Permission denied")
    return wrapper