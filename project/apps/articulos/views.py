from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . import models
from . import forms


# Create your views here.

class ArticulosCategoriaCreate(CreateView):
    model = models.ArticulosCategoria
    form_class = forms.ArticulosCategoriaForm
    success_url = reverse_lazy("articulos:index")

class ArticulosCreate(CreateView):
    model = models.Articulos
    form_class = forms.ArticulosForm
    success_url = reverse_lazy("articulos:index")
    

