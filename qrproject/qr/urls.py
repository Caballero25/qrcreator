from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateQrAPIView.as_view(), name="CreateQR"),
]