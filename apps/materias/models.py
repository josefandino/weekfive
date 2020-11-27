from django.core.validators import MinLengthValidator
from django.db import models

class Materia(models.Model):
   code = models.CharField(max_length=20)
   name = models.CharField(max_length=150, validators=[MinLengthValidator(4)])
   creditos = models.IntegerField(blank=True, null=False, validators=[MinLengthValidator(2)])
   activo = models.BooleanField(default=False)
   description = models.CharField(max_length=200, blank=True, null=False)

   class Meta:
      ordering = ['code']
      verbose_name = 'Materia'
      verbose_name_plural = 'Materias'

   def __str__(self):
      return '{0},{1}'.format(self.apellidos, self.nombre)