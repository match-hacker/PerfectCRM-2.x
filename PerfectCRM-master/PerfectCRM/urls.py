"""yumCRM URL Configuration

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
    admin_password: Aa123123
"""
from django.conf.urls import url
from django.contrib import admin
from crm import views
from PerfectCRM import views as main_views
from django.urls import include, path, re_path

urlpatterns = (
    path('admin/', admin.site.urls),
    path('crm/', include("crm.urls")),
    path('beeflow/', include("beeflow.urls")),
    path('', main_views.PortalView.as_view()),
    #url(r'^kingadmin/', include("crm.kingadmin_urls")),
    path('kingadmin/', include("kingadmin.urls")),
    path('stu/', include("student.urls")),
    path('teacher/', include("teacher.urls")),
    path('account/login/', views.acc_login),
    path('account/logout/', views.acc_logout,name='logout'),
)
