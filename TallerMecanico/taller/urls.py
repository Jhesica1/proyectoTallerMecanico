from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='inicio'),
    path('clientes/', views.ClienteListView.as_view(), name='lista_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.ClienteDeleteView.as_view(), name='eliminar_cliente'),
]

