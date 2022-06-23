from django.urls import path
from . import views

urlpatterns = [
    path('validate-profile', views.validate_profile),
    ]