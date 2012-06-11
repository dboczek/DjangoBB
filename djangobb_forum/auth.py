from djangobb_forum.models import Ban

def unbanned_user_requirement(user):
    """
    Checks that user is authenticated and not in ban list
    """
    return user.is_authenticated() and not Ban.objects.filter(user=user).exists()


def isa_forum_moderator(forum, user):
    return user.has_perm('djangobb_forum.can_moderate_forum') or user in forum.moderators.all()

