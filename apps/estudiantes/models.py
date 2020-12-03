from django.db import models

class Student(models.Model):
   nombre = models.CharField('Nombres', max_length=120, blank=True, null=False)
   apellidos = models.CharField('Apellidos', max_length=120, blank=True, null=False)
   telefono = models.CharField('Telefono', max_length=20, blank=True, null=False)
   email = models.EmailField('Email', max_length=120, blank=True, null=False)
   activo = models.BooleanField(default=False)

   

   class Meta:
      ordering = ['nombre']
      verbose_name = 'Student'
      verbose_name_plural = 'Students'

   def __str__(self):
      return '{0},{1}'.format(self.apellidos, self.nombre)
