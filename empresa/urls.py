from django.urls import path

from . import views

urlpatterns = [
    path('empresa-list', views.empresa_list, name="empresa_list"),
    path('empresa-create', views.empresa_create, name="empresa_create"),
    path('empresa-update/<int:pk>', views.empresa_update, name="empresa_update"),
    path('empresa-delete/<int:pk>', views.empresa_delete, name="empresa_delete"),
]