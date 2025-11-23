from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='inicio'),
        path('vehiculos/', views.ListaVehiculosView.as_view(), name='lista_vehiculos'),
    path('vehiculos/crear/', views.CrearVehiculoView.as_view(), name='crear_vehiculo'),
    path('vehiculos/editar/<int:pk>/', views.EditarVehiculoView.as_view(), name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:pk>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('vehiculos/detalle/<int:pk>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    # Clientes
    path('clientes/', views.ClienteListView.as_view(), name='lista_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.ClienteDeleteView.as_view(), name='eliminar_cliente'),
    # Repuestos
    path('repuestos/', views.lista_repuestos, name='lista_repuestos'),
    path('repuestos/crear/', views.crear_repuesto, name='crear_repuesto'),
    path('repuestos/editar/<int:pk>/', views.editar_repuesto, name='editar_repuesto'),
    path('repuestos/eliminar/<int:pk>/', views.eliminar_repuesto, name='eliminar_repuesto'),
]

