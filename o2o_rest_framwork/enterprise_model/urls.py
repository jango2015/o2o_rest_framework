from django.conf.urls import url
from django.contrib import admin

from .views import (
    CompanyCreateAPIView,
    CompanyDetailAPIView,
    CompanyUpdateAPIView,
    DepartmentCreateAPIView,
    CompanyHomepageView,
    PostmanagementAPIView,
    PostDenyReasonAPIView,




                    )

urlpatterns = [
    url(r'^$',CompanyHomepageView.as_view(), name='company_homepage'),
    url(r'^register/$', CompanyCreateAPIView.as_view(), name='company_create'),
    url(r'^update/(?P<pk>[\d]+)/$', CompanyUpdateAPIView.as_view(), name='company_update'),
    url(r'^(?P<pk>[\d]+)/$', CompanyDetailAPIView.as_view(), name='company_detail'),
    url(r'^create_department/$', DepartmentCreateAPIView.as_view(), name='comapny_create_department'),
    url(r'^manage_post/(?P<id>[\d]+)/(?P<method>[\w]+)$', PostmanagementAPIView.as_view(), name='manage_post'),
    url(r'^deny/(?P<pk>[\d]+)/$', PostDenyReasonAPIView.as_view(), name='company_deny_reason'),



]
'''
register:   http://127.0.0.1:8000/Company/register/
update:  http://127.0.0.1:8000/Company/update/<id>/
detail: http://127.0.0.1:8000/Company/<id>/
create department: http://127.0.0.1:8000/company/create_department/
manage_post: http://127.0.0.1:8000/company/manage_post/<id>/<method>---approve/deny
put deny reason:  http://127.0.0.1:8000/company/deny/<id>
'''