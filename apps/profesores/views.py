

from rest_framework import viewsets

from .serializers import TeacherSerializers
from .models import Teacher

class TeacherViewSet(viewsets.ModelViewSet):
   queryset = Teacher.objects.all()
   serializer_class = TeacherSerializers