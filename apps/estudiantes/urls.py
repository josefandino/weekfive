from django.urls import path

from .views import *

urlpatterns = [
   path('student/', StudentAPIView.as_view()),
   path('lacosa/', StudentView.as_view(), name='manager'),
]
