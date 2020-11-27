from django.urls import path

from .views import *

urlpatterns = [
   path('<student_id>/', StudentAPIView.as_view),
   path('', StudentView.as_view(), name='manager'),
]
