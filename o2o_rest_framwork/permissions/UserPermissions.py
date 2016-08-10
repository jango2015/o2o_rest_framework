from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    '''
    only used for change user
    '''

    message = 'you are not the original user'

    def has_object_permission(self, request, view, obj):

        return obj == request.user

class IsVarified(BasePermission):

    message = "you havn't email confirmed yet"

    def has_permission(self, request, view):
        print 'isVarified'

        return request.user.is_active

class NotAssociated(BasePermission):

    message = 'you alredy register already'

    def has_permission(self, request, view):
        if hasattr(request.user,'engineer') or hasattr(request.user,'company') or hasattr(request.user,'department'):
            return False
        else:
            print 'NotAssociated'
            return True

