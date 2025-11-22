from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm

<<<<<<< HEAD
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
=======
# Create your views here.
def pagina_principal(request):
   return render(request, 'inicio.html')
>>>>>>> 4a84c351868a018c03f5a11038bbc3130eaf6c88
