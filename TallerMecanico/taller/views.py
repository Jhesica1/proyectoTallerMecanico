from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from .models import Cliente
from .forms import ClienteForm
from .models import Repuesto
from .forms import RepuestoForm

# ------------------ Vehículos ------------------
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Vehiculo
from .forms import VehiculoForm

# Vista para listar vehículos
class ListaVehiculosView(ListView):
    model = Vehiculo
    template_name = 'lista_vehiculos.html'  # ← Cambiado
    context_object_name = 'vehiculos'
    paginate_by = 10
    
    def get_queryset(self):
        return Vehiculo.objects.filter(activo=True).order_by('-fecha_registro')

# Vista para crear vehículo
class CrearVehiculoView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo_form.html'  # ← Cambiado
    success_url = reverse_lazy('lista_vehiculos')

# Vista para editar vehículo
class EditarVehiculoView(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo_form.html'  # ← Cambiado
    success_url = reverse_lazy('lista_vehiculos')

# Vista para eliminar vehículo
def eliminar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.activo = False
        vehiculo.save()
        messages.success(request, 'Vehículo eliminado exitosamente.')
        return redirect('lista_vehiculos')
    
    return render(request, 'confirmar_eliminar.html', {'vehiculo': vehiculo})  # ← Cambiado

# Vista para ver detalles del vehículo
def detalle_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    return render(request, 'detalle_vehiculo.html', {'vehiculo': vehiculo})  # ← Cambiado

# ------------------ Clientes ------------------
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
        self.object.activo = False
        self.object.save()
        return redirect(self.success_url)


# ------------------ Página principal ------------------
def pagina_principal(request):
    return render(request, 'inicio.html')


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


def pagina_principal(request):
   return render(request, 'inicio.html')

def lista_repuestos(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'lista_repuestos.html', {'repuestos': repuestos})

def crear_repuesto(request):
    if request.method == 'POST':
        form = RepuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_repuestos')
    else:
        form = RepuestoForm()
    return render(request, 'crear_repuesto.html', {'form': form})

def editar_repuesto(request, pk):
    repuesto = get_object_or_404(Repuesto, pk=pk)
    if request.method == 'POST':
        form = RepuestoForm(request.POST, instance=repuesto)
        if form.is_valid():
            form.save()
            return redirect('lista_repuestos')
    else:
        form = RepuestoForm(instance=repuesto)
    return render(request, 'editar_repuesto.html', {'form': form})

def eliminar_repuesto(request, pk):
    repuesto = get_object_or_404(Repuesto, pk=pk)
    if request.method == 'POST':
        repuesto.delete()
        return redirect('lista_repuestos')
    return render(request, 'confirmar_eliminar_repuesto.html', {'repuesto': repuesto})