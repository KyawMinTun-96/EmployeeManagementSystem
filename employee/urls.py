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
    path('add_departments', views.add_departments, name="add-department-page"),
    path('save_department', views.save_departments, name="save-department-page"),
    path('delete-department', views.delete_departments, name="delete-department-page"),
]