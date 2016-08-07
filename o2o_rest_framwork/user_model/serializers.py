from django import forms
from rest_framework import serializers
from django.contrib.auth.models import User


class UserCreateSerializer(serializers.ModelSerializer):

    email2 = serializers.EmailField(label='comfirm_email')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
            'email2',
                  ]
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type': 'password'}
                # 'widget':serializers.ModelSerializer.widgets.PasswordInput,
            },
            'username':{'help_text':'Required. 30 characters or fewer. Letters, digits and @/./+/-/ only.'}
        }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user_obj = User(
                username = username,
                email = email,
                last_name = last_name,
                first_name = first_name,
                is_active = False,
        )
        user_obj.set_password(password)
        user_obj.save()
        print '200'
        return validated_data

    def validate(self, attrs):
        email = attrs['email']
        email2 = attrs['email2']
        username = attrs['username']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise serializers.ValidationError('repet email')
        if email != email2 :
            raise  serializers.ValidationError('the two email address is not not match')
        if '_' in username:
            raise serializers.ValidationError("can't contain '_' ")
        return attrs


class UserLogInSerialiser(serializers.ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'username',
            'password',
                  ]


    def validate(self, attrs):
        user_obj = None
        user = User.objects.filter(username=attrs['username'])
        user_obj = user.first()
        if not user_obj.check_password(attrs['password']):
            raise serializers.ValidationError('password is not right')
        return attrs


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'is_active',
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        ]

# class UserVerifySerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=True)


