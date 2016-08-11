from django.conf.urls import url
from django.contrib import admin

from .views import (
    EngineerCreateAPIView,
    EngineerDetailAPIView,
    EngineerUpdateAPIView,
    RecruitmentListAPIView


                    )

urlpatterns = [
    url(r'^register/$', EngineerCreateAPIView.as_view(), name='engineer_create'),
    url(r'^update/(?P<pk>[\d]+)/$', EngineerUpdateAPIView.as_view(), name='engineer_update'),
    url(r'^(?P<pk>[\d]+)/$', EngineerDetailAPIView.as_view(), name='engineer_detail'),
    url(r'^lists',RecruitmentListAPIView.as_view(), name='lists'),
    # url(r'^logout/$', UserLogoutAPIView.as_view(), name='logout'),
    # url(r'^confirm/(?P<email>[\S]+)/(?P<id>[\d]+)$', UserVerifyAPIView.as_view(), name='confirm'),


]
'''
register:   http://127.0.0.1:8000/engineer/register/
uodate:  http://127.0.0.1:8000/engineer/update/<id>/
detail: http://127.0.0.1:8000/engineer/<id>/
searching post:    http://127.0.0.1:8000/engineer/lists
'''