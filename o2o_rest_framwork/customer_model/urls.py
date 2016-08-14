from django.conf.urls import url
from django.contrib import admin

from .views import (
    EngineerCreateAPIView,
    EngineerDetailAPIView,
    EngineerUpdateAPIView,
    RecruitmentListAPIView,
    EngineerHomepageAPIView,
    ApplicationManagerAPIView,


                    )
from o2o_rest_framwork.order_model.views import (
    CreateApplicationAPIView
    )

urlpatterns = [
    url(r'^$',EngineerHomepageAPIView.as_view(),name='homepage'),
    url(r'^register/$', EngineerCreateAPIView.as_view(), name='engineer_create'),
    url(r'^update/(?P<pk>[\d]+)/$', EngineerUpdateAPIView.as_view(), name='engineer_update'),
    url(r'^(?P<pk>[\d]+)/$', EngineerDetailAPIView.as_view(), name='engineer_detail'),
    url(r'^lists',RecruitmentListAPIView.as_view(), name='lists'),
    url(r'^apply/(?P<id>[\d]+)$', CreateApplicationAPIView.as_view(), name='create_application'),
    url(r'^manage_app/(?P<method>[\S]+)/(?P<id>[\d]+)$', ApplicationManagerAPIView.as_view(), name='manage_app'),


]
'''
register:   http://127.0.0.1:8000/engineer/register/
uodate:  http://127.0.0.1:8000/engineer/update/<id>/
detail: http://127.0.0.1:8000/engineer/<id>/
searching post:    http://127.0.0.1:8000/engineer/lists
apply:
'''