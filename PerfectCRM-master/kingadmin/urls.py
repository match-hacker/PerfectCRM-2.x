
from django.conf.urls import url
from kingadmin import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^$', views.app_index, name="table_index"),  # 显示所有注册的表
    path('login/', views.acc_login, name="acc_login"),
    path('logout/', views.acc_logout, name="acc_logout"),
    re_path(r'^(\w+)/(\w+)/change/(\d+)/password/$', views.password_reset_form, name='password_reset'),
    path('account/password_reset/', views.personal_password_reset, name='personal_password_reset'),
    # url(r'^/$', views.app_index, name="table_index"),  # 显示所有注册的表
    re_path(r'^(\w+)/$', views.app_tables, name="app_tables"),  # 显示每个app里所有注册的表
    re_path(r'^(\w+)/(\w+)/$',views.display_table_list,name="table_list"), #显示每个表的数据
    re_path(r'^(\w+)/(\w+)/add/$', views.table_add, name="table_add"),
    re_path(r'^(\w+)/(\w+)/change/(\d+)/$', views.table_change, name="table_change"),
    re_path(r'^(\w+)/(\w+)/delete/(\d+)/$', views.table_del, name="table_del"),
]
