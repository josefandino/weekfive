from rest_framework import serializers

from .models import Materia
from ..estudiantes import Student
from ..profesores import Teacher

class MateriaSerializers(serializers.ModelSerializer):

   class Meta:
      model = Materia
      fields = '__all__'

class StudentDatosAsociadosSerializers(serializers.ModelSerializer):

   class Meta:
      model = Student
      fields = '__all__'

class TeacherDatosAsociadosSerializers(serializers.ModelSerializer):
   
   class Meta:
      model = Teacher
      fields = '__all__'