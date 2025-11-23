from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from .models import Cliente
from .forms import ClienteForm
from .models import Repuesto
from .forms import RepuestoForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Vehiculo
from .forms import VehiculoForm
from .models import ServicioUsuario
from .forms import ServicioUsuarioForm

# LISTAR
def lista_servicios(request):
    servicios = ServicioUsuario.objects.all()
    return render(request, "lista_servicios.html", {"servicios": servicios})

# CREAR
def crear_servicio(request):
    if request.method == "POST":
        form = ServicioUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_servicios')
    else:
        form = ServicioUsuarioForm()
    return render(request, "crear_servicio.html", {"form": form})

# EDITAR
def editar_servicio(request, id):
    servicio = get_object_or_404(ServicioUsuario, id=id)
    if request.method == "POST":
        form = ServicioUsuarioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect("lista_servicios")
    else:
        form = ServicioUsuarioForm(instance=servicio)
    return render(request, "editar_servicio.html", {"form": form})

# ELIMINAR
def eliminar_servicio(request, id):
    servicio = get_object_or_404(ServicioUsuario, id=id)
    if request.method == "POST":
        servicio.delete()
        return redirect("lista_servicios")
    return render(request, "eliminar_servicio.html", {"servicio": servicio})

def ver_servicio(request, pk):
    servicio = get_object_or_404(ServicioUsuario, pk=pk)
    return render(request, 'ver_servicio.html', {'servicio': servicio})

# ------------------ Vehículos ------------------


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