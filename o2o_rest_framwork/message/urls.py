from django.conf.urls import url
from django.contrib import admin

from .views import (
    MessageCreateAPIView,
    MessageRecordAPIView,
    MessageHomepageAPIView,



                    )

urlpatterns = [
    url(r'^$',MessageHomepageAPIView.as_view(), name='message_homepage'),
    # url(r'^register/$', CompanyCreateAPIView.as_view(), name='company_create'),
    url(r'^create/(?P<id>[\d]+)/$', MessageCreateAPIView.as_view(), name='message_create'),
    url(r'^record/(?P<id>[\d]+)/$', MessageRecordAPIView.as_view(), name='message_record'),
    # url(r'^(?P<pk>[\d]+)/$', CompanyDetailAPIView.as_view(), name='company_detail'),
    # url(r'^create_department/$', DepartmentCreateAPIView.as_view(), name='comapny_create_department'),
    # url(r'^manage_post/(?P<id>[\d]+)/(?P<method>[\w]+)$', PostmanagementAPIView.as_view(), name='manage_post'),
    # url(r'^deny/(?P<pk>[\d]+)/$', PostDenyReasonAPIView.as_view(), name='company_deny_reason'),



]
'''
create new message: http://127.0.0.1:8000/message/create/<id>/
message record: http://127.0.0.1:8000/message/record/<id>/
'''