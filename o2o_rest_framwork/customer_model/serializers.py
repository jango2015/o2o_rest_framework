from django import forms
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Engineer
from o2o_rest_framwork.user_model.serializers import UserDetailSerializer

class EngineerCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Engineer
        fields = [
            'phone',
            'dob',
            'ssn',
            'description',
            'major',
            'degree',
                  ]


class EngineerDetailSerializer(serializers.ModelSerializer):

    user =serializers.SerializerMethodField()

    class Meta:
        model = Engineer
        fields = [
            'user',
            'phone',
            'dob',
            'ssn',
            'description',
            'major',
            'degree',
                  ]
    def get_user(self,obj):
        user=User.objects.get(id=obj.user.id)
        return UserDetailSerializer(user,many=False).data

# class UserLogInSerialiser(serializers.ModelSerializer):
#
#     username = serializers.CharField()
#     password = serializers.CharField(style={'input_type': 'password'})
#
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'password',
#                   ]
#
#
#     def validate(self, attrs):
#         user_obj = None
#         user = User.objects.filter(username=attrs['username'])
#         user_obj = user.first()
#         if not user_obj.check_password(attrs['password']):
#             raise serializers.ValidationError('password is not right')
#         return attrs
#
#
# class UserDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             'is_active',
#             'id',
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#         ]
#
#
#
#
