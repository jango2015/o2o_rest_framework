from django import forms
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company
from o2o_rest_framwork.user_model.serializers import UserDetailSerializer
from o2o_rest_framwork.department_model.models import Department

class CompanyCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Company
        exclude = [
            'user',
            'money_amount',
            'is_approved',
        ]


class CompanyDetailSerializer(serializers.ModelSerializer):

    user =serializers.SerializerMethodField()
    bank_permit_img = serializers.SerializerMethodField()
    permit_img = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = [
                'user',
                'website',
                'phone',
                'contacter',
                'company_telphone',
                'account_bank_name',
                'money_amount',
                'bank_permit_img',
                'permit_img',
                  ]
    def get_user(self,obj):
        user=User.objects.get(id=obj.user.id)
        return UserDetailSerializer(user,many=False).data

    def get_bank_permit_img(self,obj):
        try:
            self.bank_permit_img=obj.bank_permit_img.url
        except:
            self.bank_permit_img=None
        return self.bank_permit_img

    def get_permit_img(self,obj):
        try:
            self.permit_img=obj.permit_img.url
        except:
            self.permit_img=None
        return self.permit_img


class CompanyUpdateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Company
        fields = [
        'website',
        'phone',
        'contacter',
        'company_telphone',


        ]

class DepartmentCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=30,write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Department

        fields = [
        'department_name',
        'password',
        'email',
        'phone',
        'contacter',
        'description',
        'bussiness_area',
        ]


        extra_kwargs={
            'password':{

                'style':{'input_type': 'password'}
            },

        }

    def create(self, validated_data):

        del validated_data['password']
        del validated_data['email']

        return Department.objects.create(**validated_data)

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






