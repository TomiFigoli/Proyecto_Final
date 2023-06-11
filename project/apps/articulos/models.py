from django.db import models

from django.utils import timezone
# Create your models here.
class ArticulosCategoria(models.Model):
    """Categorías de productos."""

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")

    class Meta:
        verbose_name = "categoría de Articulo"
        verbose_name_plural = "categorías de articulos"

    def __str__(self):
        """Representa una instancia de la clase como una cadena de texto."""
        return self.nombre

class Articulos(models.Model):
    # Los editores escribiran sus posteos o articulos
    titulo = models.CharField(max_length=50, unique=True)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField(max_length=2000)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de publicación")
    categoria = models.ForeignKey(ArticulosCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Categoría")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    
    def __str__(self):
        """Representa una instancia de la clase como una cadena de texto."""
        return self.titulo