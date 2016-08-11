from django.conf.urls import url
from django.contrib import admin
#
from .views import (
    DepartmentDetailAPIView,
    DepartmentEditApiView,
    RecuitmrntmentCreateAPIView,
    RecruitmentDetailAPIView,
)

urlpatterns = [
#     url(r'^register/$', CompanyCreateAPIView.as_view(), name='company_create'),
    url(r'^edit/(?P<pk>[\d]+)/$', DepartmentEditApiView.as_view(), name='department_edit'),
    url(r'^(?P<pk>[\d]+)/$', DepartmentDetailAPIView.as_view(), name='department_detail'),
    url(r'^post/(?P<pk>[\d]+)/$',RecruitmentDetailAPIView.as_view(), name='post_detail'),
    url(r'^create_post/$', RecuitmrntmentCreateAPIView.as_view(), name='department_create_post'),
    # url(r'^confirm/(?P<email>[\S]+)/(?P<id>[\d]+)$', UserVerifyAPIView.as_view(), name='confirm'),


]
'''
register:   http://127.0.0.1:8000/department/register/
edit:  http://127.0.0.1:8000/department/edit/<id>/
detail: http://127.0.0.1:8000/department/<id>/
create Recruiment Infomation: http://127.0.0.1:8000/department/create_post/
'''