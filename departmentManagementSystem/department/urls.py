from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('login_process/', views.login_process, name='login_process'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('view/', views.view, name='view'),
    path('add_department/', views.add_department, name='add_department'),
    path('manage/<int:dept_id>/', views.manage, name='manage'),
    path('delete/<int:dept_id>/', views.delete, name='delete'),
    path('list/', views.list, name='list'),
    path('export-csv/', views.export_departments_csv, name='export_csv'),
    ]

