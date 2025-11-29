from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_actividades, name='home'),
    path('actividad/add/', views.crear_actividad, name='actividad_add'),
    path('actividad/<int:pk>/edit/', views.editar_actividad, name='actividad_edit'),
    path('actividad/<int:pk>/delete/', views.borrar_actividad, name='actividad_delete'),
    path('actividad/<int:pk>/toggle/', views.toggle_actividad, name='actividad_toggle'),
]
