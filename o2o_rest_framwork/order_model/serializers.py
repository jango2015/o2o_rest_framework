from rest_framework import serializers
from .models import Application
from o2o_rest_framwork.department_model.serializers import PostDetailSerializer
from o2o_rest_framwork.user_model.serializers import UserDetailSerializer

class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields=['applier_message']

class ApplicationListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
            view_name='application-api:application_detail'
    )
    class Meta:
        model = Application
        fields=[
            'id',
            'applier_message',
            'status','applier',
            'recruitment',
            'detail',
        ]

class ApplicationDetailSerializer(serializers.ModelSerializer):

    recruitment_info = serializers.SerializerMethodField()
    applier = serializers.SerializerMethodField()
    class Meta:
        model = Application

        fields=[
            'id',
            'recruitment_info',
            'applier',
            'applier_message',
            'status','applier',
            'recruitment',
            'is_engineer_review',
            'is_department_review'
        ]

    def get_recruitment_info(self,obj):

        recruitment = obj.recruitment
        return PostDetailSerializer(recruitment,many=False).data

    def get_applier(self,obj):

        applier = obj.applier
        return UserDetailSerializer(applier,many=False).data
