from django.shortcuts import render

from rest_famework.response import Response
from rest_framework.views import APIiew
from rest_framework import status

from .models import Materia
from .serializers import (
   MateriaSerializers,
   StudentDatosAsociadosSerializers,
   TeacherDatosAsociadosSerializers,
)

class MateriaList(APIiew):

   def fet(self, request):
      materia = Materia.objects.all()
      serializer = MateriaSerializers(materia, many=True)
      return Response(serializer.data)

class MateriaBuscarId(APIiew):
   def(self, request, pk):
      materia = MateriaSerializers.filter(id=pk)
      serializer = MateriaSerializers(materia, many=True)
      return Response(serializer.data)
