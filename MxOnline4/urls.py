"""MxOnline4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import xadmin
from django.views.generic import TemplateView
from apps.users.views import LoginView
from apps.organizations.views import OrgView
from apps.courses.views import CourseView
from django.conf.urls import url,include
from django.views.static import serve
from MxOnline4.settings import MEDIA_ROOT
urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/',xadmin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('orglist/',OrgView.as_view(),name='org-list'),
    path('courselist/',CourseView.as_view(),name='course-list'),
    url(r'^org/',include(('apps.organizations.urls','organizations'),namespace='org')),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
    url(r'^course/',include(('apps.courses.urls','courses'),namespace='courses')),
]
