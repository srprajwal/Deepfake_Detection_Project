"""project_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import about, index, predict_page,cuda_full, feature, home

app_name = 'ml_app'
handler404 = views.handler404

urlpatterns = [
    path('', home, name='home'),
    path('detection/', index, name='detection'),
    path('about/', about, name='about'),
    path('feature/', feature, name='feature'),
    path('predict/', predict_page, name='predict'),
    path('cuda_full/',cuda_full,name='cuda_full'),
]
