# coding: utf-8

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index',),
    path('home/', views.home, name='home'),
    path('materiais/', views.indexMaterials, name='materials.index'),
    path('materiais/c/', views.createMaterials, name='materials.create'),
    path('materiais/e/<int:pk>/', views.editMaterials, name='materials.edit'),
    path('materiais/d/<int:pk>/', views.deleteMaterials, name='materials.delete'),
]
