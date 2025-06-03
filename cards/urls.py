from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cards/', views.card_list, name='card_list'),
    path('cards/<int:pk>/', views.card_detail, name='card_detail'),
    path('technology/<int:pk>/', views.technology_detail, name='technology_detail'),
    path('compare/', views.compare, name='compare'),
    path('api/compare/', views.compare_api, name='compare_api'),
]
