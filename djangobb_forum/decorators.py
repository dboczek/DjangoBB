from django.utils.decorators import available_attrs
from functools import wraps


def require_unbanned_user(view_func):
    """
    Marks view function to be checked by Ban middleware
    """
    def wrapped_view(*args, **kwargs):                                                                                                                                      
        return view_func(*args, **kwargs)                                                                                                                                   
    wrapped_view._unbanned_user_requirement = True
    return wraps(view_func, assigned=available_attrs(view_func))(wrapped_view) 


