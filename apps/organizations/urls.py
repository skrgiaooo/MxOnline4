
from django.conf.urls import url,include
from apps.organizations.views import OrgView,AddAsk
urlpatterns = [
    url(r'^list/',OrgView.as_view(),name='list'),
    url(r'^list/$',AddAsk.as_view())
]