from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('course/', views.course_page),
    path('register/', views.register),
    path('sikkim/',views.sikkim),
] 
