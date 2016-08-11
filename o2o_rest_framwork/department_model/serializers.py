from django import forms
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Department,RecruitmentInformation
from o2o_rest_framwork.user_model.serializers import UserDetailSerializer
from o2o_rest_framwork.department_model.models import Department
from o2o_rest_framwork.enterprise_model.serializers import CompanyDetailSerializer,Company


class DepartmentDetailSerializer(serializers.ModelSerializer):

    user =serializers.SerializerMethodField()

    company = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = [
                'user',
                'company',
                'phone',
                'contacter',
                'description',
                  ]
    def get_user(self,obj):
        user=obj.user
        return UserDetailSerializer(user,many=False).data
    def get_company(self,obj):
        company = Company.objects.get(user=obj.company)
        return CompanyDetailSerializer(company).data



class PostCreateSerialiser(serializers.ModelSerializer):

    class Meta:
        model = RecruitmentInformation
        fields = [
                  'title',
                  # 'date',
                  'description',
                  'begin_date',
                  'end_date',
                  'salary',
                  'state',
                  'city'
                  ]

class PostDetailSerializer(serializers.ModelSerializer):

    department = serializers.SerializerMethodField()
    company = serializers.SerializerMethodField()

    class Meta:

        model = RecruitmentInformation

        field = [
                  'id',
                  'department',
                  'company',
                  'title',
                  'date',
                  'description',
                  'begin_date',
                  'end_date',
                  'salary',
                  'state',
                  'city',
                  ]
    def get_department(self,obj):

        department =Department.objects.get(pk = obj.department.department.id)
        return DepartmentDetailSerializer(department,many=False).data

    def get_company(self,obj):

        department = obj.department.department
        company = Company.objects.get(id= department.company.company.id)
        return  CompanyDetailSerializer(company,many=False).data


class PostListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name= 'department-api:post_detail')
    class Meta:
        model = RecruitmentInformation

        field = [
                  'id',
                  # 'department',
                  # 'company',
                  'title',
                  'date',
                  'description',
                  'begin_date',
                  'end_date',
                  'salary',
                  'state',
                  'city',
                  'detail',
                  ]


# class CompanyUpdateSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#         model = Company
#         fields = [
#         'website',
#         'phone',
#         'contacter',
#         'company_telphone',
#
#
#         ]
#
# class DepartmentCreateSerializer(serializers.ModelSerializer):
#
#     password = serializers.CharField(max_length=30,write_only=True)
#     email = serializers.EmailField(write_only=True)
#
#     class Meta:
#         model = Department
#
#         fields = [
#         'department_name',
#         'password',
#         'email',
#         'phone',
#         'contacter',
#         'description',
#         'bussiness_area',
#         ]
#
#
#         extra_kwargs={
#             'password':{
#
#                 'style':{'input_type': 'password'}
#             },
#
#         }
#
#     def create(self, validated_data):
#
#         del validated_data['password']
#         del validated_data['email']
#
#         return Department.objects.create(**validated_data)

        # department_name = validated_data.get('department_name')
        # password = validated_data.get('password')
        # email = validated_data.get('email')
        # phone = validated_data.get('phone')
        # contacter = validated_data.get('contacter')
        # description = validated_data.get('description')
        # bussiness_area = validated_data.get('bussiness_area')
        #
        # department = Department(
        #                         user=kwargs['user'],
        #                         company=kwargs['company'],
        #                         department_name=department_name,
        #                         phone = phone,
        #                         contacter= contacter,
        #                         description=description,
        #                         bussiness_area= bussiness_area
        #                         )
        # department.save()






