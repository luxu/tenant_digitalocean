from django.urls import path

from . import views

urlpatterns = [
    path('funcionario-list', views.funcionario_list, name="funcionario_list"),
    path('funcionario-create', views.funcionario_create, name="funcionario_create"),
    path('funcionario-update/<int:pk>/', views.funcionario_update, name="funcionario_update"),
    path('funcionario-delete/<int:pk>', views.funcionario_delete, name="funcionario_delete"),
]