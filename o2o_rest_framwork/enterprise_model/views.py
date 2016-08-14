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
from .serializers import (
    CompanyCreateSerializer,
    CompanyDetailSerializer,
    CompanyUpdateSerializer,
    DepartmentCreateSerializer,
    DenyReasonSerializer,
                          )

from .models import Company
from o2o_rest_framwork.permissions.UserPermissions import NotAssociated,IsVarified
from o2o_rest_framwork.permissions.EnterprisePermissions import IsEnterprise,IsOwner,IsOwnProduct
from o2o_rest_framwork.department_model.models import Department,RecruitmentInformation
from o2o_rest_framwork.department_model.serializers import PostListSerializer,PostDetailSerializer
URL ='http://127.0.0.1:8000/'



class CompanyCreateAPIView(CreateAPIView):

    serializer_class = CompanyCreateSerializer
    permission_classes = [IsVarified,NotAssociated]
    queryset = Company.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class CompanyDetailAPIView(RetrieveAPIView):

    permission_classes = [IsVarified]
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()

class CompanyUpdateAPIView(UpdateAPIView):

    serializer_class = CompanyUpdateSerializer
    queryset = Company.objects.all()
    permission_classes = [IsVarified,IsOwner,IsEnterprise]



class DepartmentCreateAPIView(CreateAPIView):

    serializer_class = DepartmentCreateSerializer
    queryset = Department.objects.all()
    permission_classes = [IsVarified,IsOwner,IsEnterprise]

    def perform_create(self, serializer):
        department_name = serializer.validated_data.get('department_name')
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user_name = self.request.user.username + '_' +department_name
        with transaction.atomic():
            user= User.objects.create_user(username=user_name,password=password,email=email)
            serializer.save(company = self.request.user,user=user)

class CompanyHomepageView(GenericAPIView):

    permission_classes = [IsOwner,IsVarified,IsEnterprise,]

    def get(self,request):
        data = {}
        company = Company.objects.get(user=request.user)
        recruitment_info = RecruitmentInformation.objects.filter(department__department__company=company.user)
        approved_recruitment_info = recruitment_info.filter(is_varified=True)
        pending_recruitment_info = recruitment_info.filter(is_varified=False)
        denied_recruitment_info = recruitment_info.filter(is_denied=True)
        data['approved_recruitment_info']=[list for each in approved_recruitment_info]
        data['approved_recruitment_info']=PostListSerializer(approved_recruitment_info, many=True,context={'request': request}).data
        data['pending_recruitment_info']=PostListSerializer(pending_recruitment_info, many=True,context={'request': request}).data
        data['denied_recruitment_info']=PostListSerializer(denied_recruitment_info, many=True,context={'request': request}).data


        return Response(data)





class PostmanagementAPIView(GenericAPIView):


    def get(self,request,*args,**kwargs):
        # or can  use kwargs
        recruitment = RecruitmentInformation.objects.get(id = int(self.kwargs['id']))
        if self.kwargs['method'] == 'approve':
            recruitment.is_varified = True
            recruitment.save()
            return Response(PostDetailSerializer(recruitment).data)
        if self.kwargs['method'] == 'deny':
            recruitment.is_denied = True
            recruitment.save()
            data = {}
            data['message'] ='success, but do u want to give the reason od denying'
            data['url'] = URL+'company/deny/'+str(recruitment.id)
            return Response(data,status=HTTP_200_OK)

class PostDenyReasonAPIView(UpdateAPIView):

    serializer_class = DenyReasonSerializer
    queryset = RecruitmentInformation.objects.all()

