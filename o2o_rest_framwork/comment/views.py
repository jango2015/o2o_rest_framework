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
    CommentCreateSerializer,
    CommentDetailSerializer,
    CommentListSerializer,
                          )
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin
from o2o_rest_framwork.user_model.serializers import UserDetailSerializer


from .models import Comment
from o2o_rest_framwork.permissions.CommentPermissions import IsAllowtoCreateComment,IsAllowToSearch
from o2o_rest_framwork.permissions.EnterprisePermissions import IsEnterprise,IsOwner
from o2o_rest_framwork.permissions.DepartmentPermissions import DepartmentChangingOrDeletingPermission,IsDepartment
from o2o_rest_framwork.department_model.models import Department,RecruitmentInformation
from o2o_rest_framwork.department_model.serializers import PostDetailSerializer
from o2o_rest_framwork.order_model.models import Application
from o2o_rest_framwork.order_model.serializers import ApplicationListSerializer


class CommentCreateAPIView(CreateAPIView):

    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated,IsAllowtoCreateComment]

    def perform_create(self, serializer):
        application = Application.objects.get(id = self.kwargs['app_id'])
        from_user = self.request.user
        to_user_id = int(self.kwargs['id'])
        to_user = User.objects.get(id=to_user_id)
        serializer.save(from_user=from_user,to_user=to_user,application=application)


class CommentDetailAPIView(RetrieveAPIView):

    serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()


class MyCommentListAPIView(ListAPIView):

    serializer_class = CommentListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        comments = Comment.objects.filter(to_user=user)
        return comments


class SearchCommentListAPIView(ListAPIView):

    serializer_class = CommentListSerializer
    permission_classes = [IsAuthenticated,IsAllowToSearch]

    def get_queryset(self):
        id = self.kwargs['id']
        user = User.objects.get(id=int(id))
        comments = Comment.objects.filter(to_user=user)
        return comments





# class MessageRecordAPIView(ListAPIView):
#
#     serializer_class = MessageListDetailSerializer
#     permission_classes = []
#
#     def get_queryset(self):
#
#          user = self.request.user
#          sender = User.objects.get(id = self.kwargs['id'])
#
#          messages = Message.objects.filter(
#                  (
#                      Q(to_user=user) & Q(from_user=sender)
#                   )
#                  |
#                  (
#                      Q(to_user=sender) & Q(from_user=user)
#                  )
#          ).order_by('-time')[:10]
#
#          for each in messages:
#              each.is_read = True
#              each.save()
#          return  messages
#
#

