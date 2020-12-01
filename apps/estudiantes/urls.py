from django.urls import path

from .views import *

urlpatterns = [
<<<<<<< HEAD
   path('api/student/', student),
=======
   path('student/', student),
   path('lacosa/', student, name='manager'),
>>>>>>> 180eacaaae0ccb5c5c460a8cb3cc7334885dec7b
]
