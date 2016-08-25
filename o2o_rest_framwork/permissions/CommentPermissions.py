from rest_framework.permissions import BasePermission

from o2o_rest_framwork.order_model.models import Application,User

class IsCommentOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
         user = request.user
         if obj.from_user != user and obj.to_user != user:
             return False
         return True

class IsAllowtoCreateComment(BasePermission):

    '''
    if we want create duplicate comment it's not work but we didn't ban this,
    cause in the future , we might want to let user have the right to update it
    '''

    message = "you can't create the Comment cause "

    def has_permission(self, request, view):


        application_id = view.kwargs['app_id']
        to_user_id = view.kwargs['id']
        try:
            application = Application.objects.get(id=int(application_id))
            to_user = User.objects.get(id=int(to_user_id))
            if application.status != 'f':
                self.message = self.message + 'the order is still going on'
                return False
            if application.applier != request.user and application.recruitment.department != request.user:
                self.message = self.message + 'u r not ralated with this application'
                return False
            if application.applier != to_user and application.recruitment.department != to_user:
                self.message = self.message + 'the to_user is not ralated with this application'
                return False

        except:
            self.message = self.message + "we can't find this application or to_user"
            return False
        return True


class IsAllowToSearch(BasePermission):
    '''
    it's okay to search someone's comments,but we need to know if the user is exist
    '''
    message = "the user is not exist"

    def has_permission(self, request, view):
        user_id  = view.kwargs['id']
        try:
            User.objects.get(id=int(user_id))
        except:
            return False
        return True