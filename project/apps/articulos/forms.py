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

class ArticulosForm(forms.ModelForm):
    class Meta:
        model = models.Articulos
        fields = "__all__"

        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "subtitulo": forms.TextInput(attrs={"class": "form-control"}),
            "cuerpo":forms.Textarea(attrs={"class": "form-control"}),
        }