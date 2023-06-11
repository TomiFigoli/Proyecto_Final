from django.db import models

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