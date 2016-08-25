from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

class IsAllowToSendMessage(BasePermission):
    message = "the user you want send message is not exist"

    def has_permission(self, request, view):
        user_id = int(view.kwargs['id'])
        try:
            User.objects.get(id=user_id)

        except:
            return False
        return True
