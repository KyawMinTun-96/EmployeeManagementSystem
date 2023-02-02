from django.urls import URLPattern


from . import views
from django.urls import path
from django.contrib.auth import views as auth_views





urlpatterns = [
    path('', views.home, name="HomePage"),
]