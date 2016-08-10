from rest_framework.permissions import BasePermission

class IsEnterprise(BasePermission):

    message = 'you are not Enterprise'

    def has_permission(self, request, view):
        if not hasattr(request.user,'company') :
            return False
        else:
            return True
class IsOwner(BasePermission):
    message = 'you are not original user'
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user