# Describe the permissions for specific users/actions/views
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    ''' BasePermission is a predefined class from rest_framework'''
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            ''' SAFE_METHODS makes reference to every action that is not modify the object '''
            return True
        #Write permissions are only allowed to the author of a post
        return obj.author == request.user