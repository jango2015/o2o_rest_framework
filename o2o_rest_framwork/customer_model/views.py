from django.db import transaction
from django.utils.html import escape
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.filters import (
    SearchFilter,OrderingFilter ,
)
from .paginations import *
from rest_framework.generics import CreateAPIView,GenericAPIView,RetrieveAPIView,UpdateAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view
from rest_framework.permissions import (
    IsAuthenticated
)
from .serializers import(
    EngineerCreateSerializer,
    EngineerDetailSerializer
                          )
import django_filters
from rest_framework import filters
from .models import Engineer
from o2o_rest_framwork.permissions.UserPermissions import NotAssociated,IsVarified
from o2o_rest_framwork.permissions.CustomerPermissions import IsCustomer,IsOwner
from o2o_rest_framwork.department_model.models import RecruitmentInformation
from o2o_rest_framwork.department_model.serializers import PostListSerializer



class EngineerCreateAPIView(CreateAPIView):

    serializer_class = EngineerCreateSerializer
    permission_classes = [IsVarified,NotAssociated]
    queryset = Engineer.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class EngineerDetailAPIView(RetrieveAPIView):

    permission_classes = [IsVarified]
    serializer_class = EngineerDetailSerializer
    queryset = Engineer.objects.all()

class EngineerUpdateAPIView(UpdateAPIView):

    serializer_class = EngineerCreateSerializer
    queryset = Engineer.objects.all()
    permission_classes = [IsVarified,IsOwner,IsCustomer]


STATE=(('BJ','BJ'),('TJ','TJ'))
class RecruitmentFielter(filters.FilterSet):
    date_u_can_begin = django_filters.DateFilter(name='begin_date',lookup_expr='gte')
    date_u_have_to_end = django_filters.DateFilter(name='end_date',lookup_expr='lte')
    salary = django_filters.NumberFilter(name='salary',lookup_expr='gte')
    title = django_filters.CharFilter(name='title',lookup_expr='contains')
    state = django_filters.ChoiceFilter(name='state',choices=STATE)
    class Meta:
        model = RecruitmentInformation
        fields = ['title','date_u_can_begin','date_u_have_to_end','state','salary']

class RecruitmentListAPIView(ListAPIView):

    serializer_class = PostListSerializer
    permission_classes = [IsVarified]
    # filter_backends = (OrderingFilter)
    # filter_fields = ['title','begin_date','end_date','state','salary']
    filter_class =RecruitmentFielter
    queryset = RecruitmentInformation.objects.all()
    pagination_class = ListPagination


