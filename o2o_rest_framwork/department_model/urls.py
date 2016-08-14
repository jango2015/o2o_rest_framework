from django.conf.urls import url
from django.contrib import admin
#
from .views import (
    DepartmentDetailAPIView,
    DepartmentEditApiView,
    RecuitmrntmentCreateAPIView,
    RecruitmentDetailAPIView,
    DepartmentHomepageAPIView,
    ApplicationManagerAPIView,
)

urlpatterns = [
    url(r'^$', DepartmentHomepageAPIView.as_view(), name='department_homepage'),
    url(r'^edit/(?P<pk>[\d]+)/$', DepartmentEditApiView.as_view(), name='department_edit'),
    url(r'^(?P<pk>[\d]+)/$', DepartmentDetailAPIView.as_view(), name='department_detail'),
    url(r'^post/(?P<pk>[\d]+)/$',RecruitmentDetailAPIView.as_view(), name='post_detail'),
    url(r'^create_post/$', RecuitmrntmentCreateAPIView.as_view(), name='department_create_post'),
    url(r'^manage_app/(?P<method>[\S]+)/(?P<id>[\d]+)$', ApplicationManagerAPIView.as_view(), name='manage_app'),
    # url(r'^confirm/(?P<email>[\S]+)/(?P<id>[\d]+)$', UserVerifyAPIView.as_view(), name='confirm'),


]
'''
homrpage:   http://127.0.0.1:8000/department/
register:   http://127.0.0.1:8000/department/register/
edit:  http://127.0.0.1:8000/department/edit/<id>/
detail: http://127.0.0.1:8000/department/<id>/
create Recruiment Infomation: http://127.0.0.1:8000/department/create_post/
manage app:     http://127.0.0.1:8000/department/manage_app/(?P<method>[\S]+)/(?P<id>[\d]+)
'''