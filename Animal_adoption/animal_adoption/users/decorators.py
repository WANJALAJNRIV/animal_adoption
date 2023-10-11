from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def user_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if request.user.role == 'user':
            return function(request, *args, **kwargs)
        else:
            messages.error(request, 'Permission denied.')
            return redirect('permission_denied_page')  # Redirect to a permission denied page
    return wrapper




def user_or_admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role in ['user', 'admin']:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'Permission denied.')
            return redirect('permission_denied_page')

    return _wrapped_view
