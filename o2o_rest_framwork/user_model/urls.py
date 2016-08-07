from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLogInAPIView,
    UserDetailAPIView,
    UserVerifyAPIView,
    UserLogoutAPIView,
    )

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^login/$', UserLogInAPIView.as_view(), name='login'),
    url(r'^(?P<pk>[\d]+)/$', UserDetailAPIView.as_view(), name='detail'),
    # url(r'^confirm',UserLogInAPIView, name='confirm'),
    url(r'^logout/$', UserLogoutAPIView.as_view(), name='logout'),
    url(r'^confirm/email/(?P<email>[\S]+)/id/(?P<id>[\d]+)$', UserVerifyAPIView.as_view(), name='confirm'),


]