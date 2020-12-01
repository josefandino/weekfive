from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status

from django.views.generic import View
from django.shortcuts import render

from .serializers import StudentSerializers
from .models import Student


@api_view(['GET', 'POST', 'DELETE'])
def student(request):
<<<<<<< HEAD
   if request.method == 'GET':
      students = Student.objects.all()
      serialized = StudentSerializers(students, many=True)
      return Response(status=HTTP_200_OK, data=serialized.data)
   
   if request.method == 'POST':
      students = StudentSerializers(data=request.data)
      if student.is_valid():
         return Response(status=HTTP_201_CREATED)
      else:
         return Response(status=HTTP_400_BAD_REQUEST, data=student.errors)

class StudentView(View):
   model = Student
   template_name = "students/listado.html"

# class StudentAPIView(generics.ListCreateAPIView):
#    queryset = Student.objects.all()
#    serializer_class = StudentSerializers

=======
    if request.method == 'GET':
        students = Student.objects.all()
        serialized = StudentSerializers(students, many=True)
        return Response(status=HTTP_200_OK, data=serialized.data)

    if request.method == 'POST':
        students = StudentSerializers(data=request.data)
        if student.is_valid():
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST, data=students.errors)

# class StudentView(View):
#    model = Student
#    template_name = "students/listado.html"
#
# class StudentAPIView(generics.ListCreateAPIView):
#    queryset = Student.objects.all()
#    serializer_class = StudentSerializers
#
>>>>>>> 180eacaaae0ccb5c5c460a8cb3cc7334885dec7b
#    def list(self, request):
#       queryset = self.get_queryset()
#       serializer = StudentSerializers(queryset, many=True)
#       return Response(serializer.data)
<<<<<<< HEAD
      


=======
#
#
>>>>>>> 180eacaaae0ccb5c5c460a8cb3cc7334885dec7b
