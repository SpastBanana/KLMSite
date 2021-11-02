from django.urls import path
from . import views

urlpatterns = [
    path('', views.startView, name='start-instructions'),
    path('instructions/', views.startView, name='start-instructions'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('system-info/', views.systemView, name='system-info'),
]
