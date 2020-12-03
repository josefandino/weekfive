from rest_framework.decorators import action
from rest_framework import viewsets

from .serializers import MateriaSerializers
from .models import Materia

class MateriaViewSet(viewsets.ModelViewSet):
   queryset = Materia.objects.all()
   serializer_class = MateriaSerializers

   # @action(methods=['GET'], detail=True)
   # def materia(self, request, pk=None):
   #    materia = self.get.object()
   #    serializer = MateriaSerializers(materia.autores, many=True)
   #    return Response(status.HTTP_200_OK, data=serializer_class.data)



