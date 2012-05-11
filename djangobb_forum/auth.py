from djangobb_forum.models import Ban

def unbanned_user_requirement(user):
    """
    Checks that user is authenticated and not in ban list
    """
    return user.is_authenticated() and not Ban.objects.filter(user=user).exists()
