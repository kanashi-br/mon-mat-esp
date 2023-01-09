# coding: utf-8

from django.urls import path
from . import views
from .views import ErrorPage

urlpatterns = [
    path('', views.index, name='index',),
    path('home/', views.home, name='home'),
    path('materiais/', views.indexMaterials, name='materials.index'),
    path('materiais/c/', views.createMaterials, name='materials.create'),
    path('materiais/e/<int:pk>/', views.editMaterials, name='materials.edit'),
    path('materiais/d/<int:pk>/', views.deleteMaterials, name='materials.delete'),
    path('emprestimos/', views.indexLoans, name='loans.index'),
    path('emprestimos/c/', views.createLoans, name='loans.create'),
    path('emprestimos/e/<int:pk>/', views.editLoans, name='loans.edit'),
    path('emprestimos/d/<int:pk>/', views.deleteLoans, name='loans.delete'),
    
    path(r'^error_page/$', ErrorPage.as_view(), name="error-page"),

]
