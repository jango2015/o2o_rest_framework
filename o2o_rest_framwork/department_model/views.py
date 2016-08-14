from datetime import datetime



from django.db import transaction
from django.utils.html import escape
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from rest_framework.generics import CreateAPIView,GenericAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.reverse import reverse_lazy

from .serializers import (
    DepartmentDetailSerializer,
    PostCreateSerialiser,
    PostDetailSerializer,
    PostListSerializer,
                          )
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin


from .models import Department
from o2o_rest_framwork.permissions.UserPermissions import NotAssociated,IsVarified
from o2o_rest_framwork.permissions.EnterprisePermissions import IsEnterprise,IsOwner
from o2o_rest_framwork.permissions.DepartmentPermissions import DepartmentChangingOrDeletingPermission,IsDepartment
from o2o_rest_framwork.department_model.models import Department,RecruitmentInformation
from o2o_rest_framwork.department_model.serializers import PostDetailSerializer
from o2o_rest_framwork.order_model.models import Application
from o2o_rest_framwork.order_model.serializers import ApplicationListSerializer


# class CompanyCreateAPIView(CreateAPIView):
#
#     serializer_class = CompanyCreateSerializer
#     permission_classes = [IsVarified,NotAssociated]
#     queryset = Company.objects.all()
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)



class DepartmentDetailAPIView(UpdateModelMixin,RetrieveAPIView):

    permission_classes = [IsVarified]
    serializer_class = DepartmentDetailSerializer
    queryset = Department.objects.all()


class DepartmentEditApiView(UpdateModelMixin,DestroyModelMixin,RetrieveAPIView):

    permission_classes = [DepartmentChangingOrDeletingPermission]
    serializer_class = DepartmentDetailSerializer
    queryset = Department.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)


class RecuitmrntmentCreateAPIView(CreateAPIView):

    permission_classes = [IsDepartment]
    serializer_class = PostCreateSerialiser
    queryset = RecruitmentInformation

    def perform_create(self, serializer):
        instance = serializer.save(department= self.request.user ,date=datetime.today().date())

class RecruitmentDetailAPIView(RetrieveAPIView):

    permission_classes = [IsVarified]
    serializer_class = PostDetailSerializer
    queryset = RecruitmentInformation.objects.all()


class DepartmentHomepageAPIView(GenericAPIView):
    permission_classes = [IsVarified,IsDepartment,IsOwner]

    def get(self,request):
        recruitment_info=RecruitmentInformation.objects.filter(department=request.user)
        data={}
        approved_recruitment_info = recruitment_info.filter(is_varified=True)
        pending_recruitment_info = recruitment_info.filter(is_varified=False)
        denied_recruitment_info = recruitment_info.filter(is_denied=True)
        applications = Application.objects.filter_by_department(user=request.user)
        applying = applications.filter(status='w')
        pending = applications.filter(status='s')
        data['approved_recruitment_info']=[list for each in approved_recruitment_info]
        data['approved_recruitment_info']=PostListSerializer(approved_recruitment_info, many=True,context={'request': request}).data
        data['pending_recruitment_info']=PostListSerializer(pending_recruitment_info, many=True,context={'request': request}).data
        data['denied_recruitment_info']=PostListSerializer(denied_recruitment_info, many=True,context={'request': request}).data
        data['applying'] = ApplicationListSerializer(applying,many=True,context={'request': request}).data
        data['pending'] = ApplicationListSerializer(pending,many=True,context={'request': request}).data
        #cause in our serializers, we called anther funcyions so we must have context={'request': request}


        data['revers test']=reverse_lazy('users-api:login',request=request)

        return Response(data)



class ApplicationManagerAPIView(GenericAPIView):

    def get(self,request,*args,**kwargs):
        method = self.kwargs['method']
        id = self.kwargs['id']

        application = Application.objects.get(id=id)

        if method == 'approve':
            if application.status != 'w':
                return Response(HTTP_400_BAD_REQUEST)
            recruitment_info = application.recruitment
            recruitment_info.is_over = True
            recruitment_info.save()
            application.status = 'a'
            application.save()

        if method == 'finish':

            if application.status != 's':
                return Response(HTTP_400_BAD_REQUEST)

            application.status = 'f'
            application.save()

        if method == 'deny':
            if application.status != 'w':
                return Response(HTTP_400_BAD_REQUEST)
            application.status = 'd'
            application.save()

        return Response(HTTP_200_OK)





#
# class DepartmentCreateAPIView(CreateAPIView):
#
#     serializer_class = DepartmentCreateSerializer
#     queryset = Department.objects.all()
#     permission_classes = [IsVarified,IsOwner,IsEnterprise]
#
#     def perform_create(self, serializer):
#         department_name = serializer.validated_data.get('department_name')
#         email = serializer.validated_data.get('email')
#         password = serializer.validated_data.get('password')
#         user_name = self.request.user.username + '_' +department_name
#         with transaction.atomic():
#             user= User.objects.create_user(username=user_name,password=password,email=email)
#             serializer.save(company = self.request.user,user=user)


