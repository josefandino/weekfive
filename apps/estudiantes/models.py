from django.db import models


   class Meta:
      ordering = ['nombre']
      verbose_name = 'Student'
      verbose_name_plural = 'Students'

   def __str__(self):
      return '{0},{1}'.format(self.apellidos, self.nombre)
