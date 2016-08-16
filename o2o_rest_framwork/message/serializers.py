from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message
from o2o_rest_framwork.user_model.serializers import UserDetailSerializer
from o2o_rest_framwork.department_model.models import Department,RecruitmentInformation


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['content']

class MessageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = [
            'time',
            'from_user',
            'to_user',
        ]
class MessageListDetailSerializer(serializers.ModelSerializer):
    reply_id = serializers.SerializerMethodField()
    class Meta:
        model = Message
        fields = [
            'reply_id',
            'content',
            'time',
            'from_user',
            'to_user',
        ]

    def get_reply_id(self,obj):
        return obj.from_user.id