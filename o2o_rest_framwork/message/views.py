from datetime import datetime


from django.db.models import Q
from django.db import transaction
from django.utils.html import escape
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from rest_framework.generics import CreateAPIView,GenericAPIView,RetrieveAPIView,UpdateAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.reverse import reverse_lazy

from .serializers import (
    MessageCreateSerializer,
    MessageListDetailSerializer,
    MessageListSerializer,
                          )
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin
from o2o_rest_framwork.user_model.serializers import UserDetailSerializer


from .models import Message
from o2o_rest_framwork.permissions.UserPermissions import NotAssociated,IsVarified
from o2o_rest_framwork.permissions.EnterprisePermissions import IsEnterprise,IsOwner
from o2o_rest_framwork.permissions.DepartmentPermissions import DepartmentChangingOrDeletingPermission,IsDepartment
from o2o_rest_framwork.department_model.models import Department,RecruitmentInformation
from o2o_rest_framwork.department_model.serializers import PostDetailSerializer
from o2o_rest_framwork.order_model.models import Application
from o2o_rest_framwork.order_model.serializers import ApplicationListSerializer


class MessageCreateAPIView(CreateAPIView):

    serializer_class = MessageCreateSerializer
    permission_classes = []

    def perform_create(self, serializer):
        from_user = self.request.user
        to_user_id = int(self.kwargs['id'])
        to_user = User.objects.get(id = to_user_id)
        serializer.save(from_user=from_user,to_user=to_user)

class MessageHomepageAPIView(GenericAPIView):

    permission_classes = []

    def get(self,request,*args,**kwargs):
        messages =  Message.objects.filter(Q(to_user=request.user)|Q(from_user=request.user))
        received_message =messages.filter(to_user=request.user)
        unread_message = received_message.filter(is_read=False)
        count_of_unread_messages = unread_message.count()
        recent_contactor_ids = received_message.values_list('from_user').distinct()
        recent_contactor=User.objects.filter(id__in=recent_contactor_ids)

        data={}
        data['count_of_unread_messages'] = count_of_unread_messages
        data['unread_message'] = MessageListSerializer(unread_message,many=True).data
        data['recent_contactor'] = UserDetailSerializer(recent_contactor,many=True).data

        return Response(data,HTTP_200_OK)


class MessageRecordAPIView(ListAPIView):

    serializer_class = MessageListDetailSerializer
    permission_classes = []

    def get_queryset(self):

         user = self.request.user
         sender = User.objects.get(id = self.kwargs['id'])

         messages = Message.objects.filter(
                 (
                     Q(to_user=user) & Q(from_user=sender)
                  )
                 |
                 (
                     Q(to_user=sender) & Q(from_user=user)
                 )
         ).order_by('-time')[:10]

         for each in messages:
             each.is_read = True
             each.save()
         return  messages



