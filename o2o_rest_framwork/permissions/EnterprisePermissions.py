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
        print obj.user
        return obj.user == request.user


class IsOwnProduct(BasePermission):

    message = "that's not your product"

    def has_object_permission(self, request, view, obj):
        if obj.department.department.company != request.user:
            print obj.department.department.company
            print request.user
            return False

        return True
