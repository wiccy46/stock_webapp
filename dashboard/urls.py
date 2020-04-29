from django.urls import path

from . import views 

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('prices/', views.prices, name='prices'),
    path('settings/', views.settings, name='settings'),
]