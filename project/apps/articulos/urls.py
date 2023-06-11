from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="articulos/index.html"), name="index"),
    path("articuloscategoria/create/", views.ArticulosCategoriaCreate.as_view(), name="articulos_categoria_create"),
    path("articulos/create", views.ArticulosCreate.as_view(), name="articulos_create"),
]