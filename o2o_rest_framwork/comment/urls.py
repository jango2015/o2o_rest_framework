from django.conf.urls import url
from django.contrib import admin

from .views import (
    CommentCreateAPIView,
    CommentDetailAPIView,
    MyCommentListAPIView,
    SearchCommentListAPIView,
    )

urlpatterns = [
    url(r'^$',MyCommentListAPIView.as_view(), name='my_comments'),
    # url(r'^register/$', CompanyCreateAPIView.as_view(), name='company_create'),
    url(r'^create/(?P<id>[\d]+)/(?P<app_id>[\d]+)/$', CommentCreateAPIView.as_view(), name='comment_create'),
    url(r'^(?P<pk>[\d]+)/$', CommentDetailAPIView.as_view(), name='comment_detail'),
    url(r'^search/(?P<id>[\d]+)/$', SearchCommentListAPIView.as_view(), name='search_comment'),
    # url(r'^create_department/$', DepartmentCreateAPIView.as_view(), name='comapny_create_department'),
    # url(r'^manage_post/(?P<id>[\d]+)/(?P<method>[\w]+)$', PostmanagementAPIView.as_view(), name='manage_post'),
    # url(r'^deny/(?P<pk>[\d]+)/$', PostDenyReasonAPIView.as_view(), name='company_deny_reason'),



]
'''

create new comment : http://127.0.0.1:8000/comment/create/<id>/<app_id>/
my own reciew: http://127.0.0.1:8000/comment/
comment Detail: http://127.0.0.1:8000/comment/<id>/
look other user's comment :http://127.0.0.1:8000/comment/search/<user_id>/
'''