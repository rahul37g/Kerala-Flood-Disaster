"""Kerala_Support URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from kerala_supportapp import views as KeralaSupportApp_views
from django.conf import settings
admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', KeralaSupportApp_views.login_user),
    url(r'^logout/', KeralaSupportApp_views.logout_view),

    url(r'^fetch_delete_update_language_master/(?P<language_id>[\w\-].+)/$', KeralaSupportApp_views.LanguageMasterGetView.as_view()),
    url(r'^fetch_language_master_list', KeralaSupportApp_views.LanguageMasterListView.as_view()),
    url(r'^post_language_master/$', KeralaSupportApp_views.LanguageMasterPostView.as_view()),

    url(r'^fetch_delete_update_service_type_master/(?P<service_type_id>[\w\-].+)/$', KeralaSupportApp_views.ServiceTypeMasterGetView.as_view()),
    url(r'^fetch_service_type_master_list', KeralaSupportApp_views.ServiceTypeMasterListView.as_view()),
    url(r'^post_service_type_master/$', KeralaSupportApp_views.ServiceTypeMasterPostView.as_view()),

    url(r'^fetch_delete_update_emergency_type_master/(?P<emergency_type_id>[\w\-].+)/$', KeralaSupportApp_views.EmergencyTypeMasterGetView.as_view()),
    url(r'^fetch_emergency_type_master_list', KeralaSupportApp_views.EmergencyTypeMasterListView.as_view()),
    url(r'^post_emergency_type_master/$', KeralaSupportApp_views.EmergencyTypeMasterPostView.as_view()),

    url(r'^fetch_delete_update_service_master/(?P<service_id>[\w\-].+)/$', KeralaSupportApp_views.ServiceMasterGetView.as_view()),
    url(r'^fetch_service_master_list', KeralaSupportApp_views.ServiceMasterListView.as_view()),
    url(r'^post_service_master/$', KeralaSupportApp_views.ServiceMasterPostView.as_view()),


    url(r'^fetch_delete_update_employee_master/(?P<employee_id>[\w\-].+)/$', KeralaSupportApp_views.EmployeeMasterGetView.as_view()),
    url(r'^fetch_employee_master_list', KeralaSupportApp_views.EmployeeMasterListView.as_view()),
    url(r'^post_employee_master/$', KeralaSupportApp_views.EmployeeMasterPostView.as_view()),


    url(r'^fetch_delete_update_location_type_master/(?P<location_type_id>[\w\-].+)/$', KeralaSupportApp_views.LocationTypeMasterGetView.as_view()),
    url(r'^fetch_location_type_master_list', KeralaSupportApp_views.LocationTypeMasterListView.as_view()),
    url(r'^post_location_type_master/$', KeralaSupportApp_views.LocationTypeMasterPostView.as_view()),


    url(r'^fetch_delete_update_location_master/(?P<location_type_id>[\w\-].+)/$', KeralaSupportApp_views.LocationMasterGetView.as_view()),
    url(r'^fetch_location_master_list', KeralaSupportApp_views.LocationMasterListView.as_view()),
    url(r'^post_location_master/$', KeralaSupportApp_views.LocationMasterPostView.as_view()),

    url(r'^fetch_delete_update_status_master/(?P<status_id>[\w\-].+)/$', KeralaSupportApp_views.StatusMasterGetView.as_view()),
    url(r'^fetch_status_master_list', KeralaSupportApp_views.StatusMasterListView.as_view()),
    url(r'^post_status_master/$', KeralaSupportApp_views.StatusMasterPostView.as_view()),

    url(r'^fetch_delete_update_service_transaction/(?P<service_transaction_id>[\w\-].+)/$', KeralaSupportApp_views.ServiceRequiredTransactionGetView.as_view()),
    url(r'^fetch_service_transaction_list', KeralaSupportApp_views.ServiceRequiredTransactionListView.as_view()),
    url(r'^post_service_transaction/$', KeralaSupportApp_views.ServiceRequiredTransactionPostView.as_view()),

    url(r'^fetch_delete_update_team_master/(?P<team_id>[\w\-].+)/$', KeralaSupportApp_views.TeamMasterGetView.as_view()),
    url(r'^fetch_team_master_list', KeralaSupportApp_views.TeamMasterListView.as_view()),
    url(r'^post_team_master/$', KeralaSupportApp_views.TeamMasterPostView.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)
