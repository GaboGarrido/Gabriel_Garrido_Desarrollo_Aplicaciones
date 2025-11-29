from django.db import models

class Actividad(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    completada = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
    
    def __str__(self):
        return self.titulo
