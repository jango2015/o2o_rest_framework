from rest_framework import serializers
from .models import Comment
from o2o_rest_framwork.order_model.serializers import ApplicationDetailSerializer
class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'starts',
            'review',
        ]


class CommentListSerializer(serializers.ModelSerializer):
    application_name = serializers.SerializerMethodField()
    application_id = serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(view_name='comment-api:comment_detail')

    class Meta:
        model = Comment
        fields = [
            'application_name',
            'starts',
            'review',
            'from_user',
            'to_user',
            'date',
            'application_id',
            'detail',
        ]


    def get_application_name(self,obj):
        return obj.application.recruitment.title

    def get_application_id(self,obj):
        return obj.application.id


class CommentDetailSerializer(serializers.ModelSerializer):
    application = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'application',
            'starts',
            'review',
            'from_user',
            'to_user',
            'date',
        ]

    def get_application(self,obj):

        application = obj.application

        return ApplicationDetailSerializer(application, many=False).data