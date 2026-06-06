from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('founder/', views.founder, name='founder'),
    path('register/', views.customer_register, name='customer_register'),
]
