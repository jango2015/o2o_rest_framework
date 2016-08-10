from django.conf.urls import url
from django.contrib import admin

from .views import (
    CompanyCreateAPIView,
    CompanyDetailAPIView,
    CompanyUpdateAPIView,
    DepartmentCreateAPIView,


                    )

urlpatterns = [
    url(r'^register/$', CompanyCreateAPIView.as_view(), name='company_create'),
    url(r'^update/(?P<pk>[\d]+)/$', CompanyUpdateAPIView.as_view(), name='company_update'),
    url(r'^(?P<pk>[\d]+)/$', CompanyDetailAPIView.as_view(), name='company_detail'),
    # url(r'^confirm',UserLogInAPIView, name='confirm'),
    url(r'^create_department/$', DepartmentCreateAPIView.as_view(), name='comapny_create_department'),
    # url(r'^confirm/(?P<email>[\S]+)/(?P<id>[\d]+)$', UserVerifyAPIView.as_view(), name='confirm'),


]
'''
register:   http://127.0.0.1:8000/Company/register/
uodate:  http://127.0.0.1:8000/Company/update/<id>/
detail: http://127.0.0.1:8000/Company/<id>/
create department: http://127.0.0.1:8000/company/create_department/
'''