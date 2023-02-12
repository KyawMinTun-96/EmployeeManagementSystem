from django.urls import URLPattern
from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView



urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"), name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('login', auth_views.LoginView.as_view(template_name = 'ems_info/login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),
    path('positions', views.positions, name="position-page"),
    path('add_position', views.add_positions, name="add-position-page"),
    path('save_position', views.save_positions, name="save-position-page"),
    path('delete-position', views.delete_positions, name="delete-position-page"),
    path('departments', views.departments, name="department-page"),
    path('add_department', views.add_departments, name="add-department-page"),
    path('save_department', views.save_departments, name="save-department-page"),
    path('delete-department', views.delete_departments, name="delete-department-page"),
    path('employees', views.employees, name="employee-page"),
    path('add_employee', views.add_employees, name="add-employee-page"),
    path('save_employee', views.save_employees, name="save-employee-page"),
    path('delete-employee', views.delete_employees, name="delete-employee-page"),
    path('view_employee', views.view_employee, name="view-employee"),
    path('projects', views.projects, name="project-page"),
    path('add_project', views.add_projects, name="add-project-page"),
    path('save_project', views.save_projects, name='save-project-page'),
    path('delete_project', views.delete_projects, name="delete-project-page"),
    path('view_project', views.view_project, name="view-project-page"),
]