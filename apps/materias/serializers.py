from rest_framework import serializers

from .models import Materia

class MateriaSerializers(serializers.ModelSerializer):
   class Meta:
      model = Materia
      fields = ['code','name','creditos','activo','description']
      
