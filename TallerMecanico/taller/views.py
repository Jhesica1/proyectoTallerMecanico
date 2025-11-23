
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm
from .models import Vehiculo
from .forms import VehiculoForm


class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'lista_vehiculos.html'
    context_object_name = 'vehiculos'

    def get_queryset(self):
        return Vehiculo.objects.filter(activo=True)

def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'crear_vehiculo.html', {'form': form})

def editar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'editar_vehiculo.html', {'form': form, 'vehiculo': vehiculo})

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    template_name = 'confirmar_eliminar_vehiculo.html'
    success_url = reverse_lazy('lista_vehiculos')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return redirect(self.success_url)



class ClienteListView(ListView):
    model = Cliente
    template_name = 'lista_clientes.html'
    context_object_name = 'clientes'
    
    def get_queryset(self):
        return Cliente.objects.filter(activo=True)


def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'crear_cliente.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'editar_cliente.html', {'form': form, 'cliente': cliente})

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'confirmar_eliminar_cliente.html'
    success_url = reverse_lazy('lista_clientes')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # En lugar de eliminar, marcamos como inactivo
        self.object.activo = False
        self.object.save()
        return redirect(self.success_url)


class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/lista_clientes.html'
    context_object_name = 'clientes'
    
    def get_queryset(self):
        return Cliente.objects.filter(activo=True)

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'clientes/crear_cliente.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'clientes/editar_cliente.html', {'form': form, 'cliente': cliente})

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/confirmar_eliminar_cliente.html'
    success_url = reverse_lazy('lista_clientes')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # En lugar de eliminar, marcamos como inactivo
        self.object.activo = False
        self.object.save()
        return redirect(self.success_url)
# Create your views here.
def pagina_principal(request):
   return render(request, 'inicio.html')

