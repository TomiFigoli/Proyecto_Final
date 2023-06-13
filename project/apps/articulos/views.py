from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . import models
from . import forms


# Create your views here.
# categorias
class ArticulosCategoriaCreate(CreateView):
    model = models.ArticulosCategoria
    form_class = forms.ArticulosCategoriaForm
    success_url = reverse_lazy("articulos:index")

class ArticuloCategoriaList(ListView):
    model = models.ArticulosCategoria

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.ArticulosCategoria.objects.filter(nombre__icontains=query)
        else:
            object_list = models.ArticulosCategoria.objects.all()
        return object_list

class ArticuloCategoriaDetail(DetailView):
    model = models.ArticulosCategoria
# articulos

class ArticulosCreate(CreateView):
    model = models.Articulos
    form_class = forms.ArticulosForm
    success_url = reverse_lazy("articulos:index")

class ArticuloDetail(DetailView):
    model = models.Articulos


    

