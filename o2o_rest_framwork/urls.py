"""o2o_rest_framwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('o2o_rest_framwork.user_model.urls', namespace='users-api')),
    url(r'^engineer/', include('o2o_rest_framwork.customer_model.urls', namespace='engineer-api')),
    url(r'^company/', include('o2o_rest_framwork.enterprise_model.urls', namespace='enterprise-api')),
    url(r'^department/', include('o2o_rest_framwork.department_model.urls', namespace='department-api')),
    url(r'^application/',include('o2o_rest_framwork.order_model.urls',namespace='application-api')),
]
