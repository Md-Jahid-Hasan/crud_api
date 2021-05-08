from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Restrict user to edit other profile"""

    def has_object_permission(self, request, view, obj):
        """Return True if user try to return own profile"""
        """SAFE_METHOD has all the HTTP method that can visible by all ex. get()"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id