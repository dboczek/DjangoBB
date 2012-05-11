
def require_unbanned_user(view_func):
    """
    Marks view function to be checked by Ban middleware
    """
    view_func._unbanned_user_requirement = True
    return view_func


