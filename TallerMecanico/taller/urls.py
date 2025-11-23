from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='inicio'),
    path('clientes/', views.ClienteListView.as_view(), name='lista_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.ClienteDeleteView.as_view(), name='eliminar_cliente'),
    path('', views.pagina_principal, name='inicio'),
    
    path('', views.VehiculoListView.as_view(), name='lista_vehiculos'),
    path('crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('editar/<int:pk>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('eliminar/<int:pk>/', views.VehiculoDeleteView.as_view(), name='eliminar_vehiculo'),
]

