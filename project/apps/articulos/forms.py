from django import forms

from . import models

class ArticulosCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ArticulosCategoria
        fields = "__all__"

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }