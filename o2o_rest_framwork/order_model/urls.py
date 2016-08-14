from django.conf.urls import url
from django.contrib import admin

from .views import (
    ApplicationDetailAPIView


                    )

urlpatterns = [
#     url(r'^$',CompanyHomepageView.as_view(), name='company_homepage'),
#     url(r'^register/$', CompanyCreateAPIView.as_view(), name='company_create'),
#     url(r'^update/(?P<pk>[\d]+)/$', CompanyUpdateAPIView.as_view(), name='company_update'),
    url(r'^(?P<pk>[\d]+)/$', ApplicationDetailAPIView.as_view(), name='application_detail'),
    # url(r'^create_department/$', DepartmentCreateAPIView.as_view(), name='comapny_create_department'),
    # url(r'^manage_post/(?P<id>[\d]+)/(?P<method>[\w]+)$', PostmanagementAPIView.as_view(), name='manage_post'),
    # url(r'^deny/(?P<pk>[\d]+)/$', PostDenyReasonAPIView.as_view(), name='company_deny_reason'),


]
'''

detail: http://127.0.0.1:8000/application/<id>/

'''