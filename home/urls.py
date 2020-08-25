from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about/', views.about, name='home-about'),
    path('projects/', views.projects, name='home-projects'),
    path('misc/', views.misc, name='home-misc'),
    path('misc/gradientGen/', views.gradient, name='home-misc-gradient'),
]
