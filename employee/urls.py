from django.urls import URLPattern
from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView



urlpatterns = [
    path('', views.home, name="home-page"),
    path('departments', views.departments, name="department-page"),
    path('positions', views.positions, name="position-page"),
    path('employees', views.employees, name="employee-page"),
    path('projects', views.projects, name="project-page"),
    path('save_department', views.save_departments, name="save-department-page"),
    path('save_position', views.save_positions, name="save-position-page"),
    path('save_employee', views.save_employees, name="save-employee-page"),
    path('delete-department', views.delete_departments, name="delete-department-page"),
    path('delete-position', views.delete_positions, name="delete-position-page"),
    path('delete-employee', views.delete_employees, name="delete-employee-page"),
    path('add_department', views.add_departments, name="add-department-page"),
    path('add_position', views.add_positions, name="add-position-page"),
    path('add_employee', views.add_employees, name="add-employee-page"),
    path('view_employee', views.view_employee, name="view-employee"),
]