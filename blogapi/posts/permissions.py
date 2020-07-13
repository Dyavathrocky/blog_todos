from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #read only permissions allowed for any useres
        if request.method in permissions.SAFE_METHODS:
            return True

        #writer permissions are only allowed to the author of a post
        return obj.author == request.user