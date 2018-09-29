
from django.urls import path, re_path
from crm import views

urlpatterns = [
    path('', views.sales_dashboard, name="crm_dashboard"), #销售角色首页
    path('customers/', views.customers, name="customers"),
    re_path('customers/change/(\d+)/$', views.customer_change, name="customer_change"),
    path('my_customers/', views.my_customers, name="my_customers"),
    path('sales_report/', views.sales_report, name="sales_report"),
    re_path('enrollment/(\d+)/$', views.enrollment, name="enrollment"),
    re_path('enrollment/stu/(\d+)/$', views.stu_enrollment, name="stu_enrollment"),
]
