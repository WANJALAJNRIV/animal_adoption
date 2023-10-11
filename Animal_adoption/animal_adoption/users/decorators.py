from functools import wraps
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse


def user_required(function):
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