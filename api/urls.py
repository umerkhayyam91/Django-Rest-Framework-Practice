from django.urls import path
from . import views

urlpatterns = [
    path('getItems/', views.getItems),
    path('addItems/', views.addItems),
]