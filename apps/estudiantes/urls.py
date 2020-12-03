# from django.urls import path

# from .views import *

# urlpatterns = [
#    path('student/', student),
#    path('lacosa/', student, name='manager'),
# ]

from rest_framework.routers import DefaultRouter

from .views import StudentViewSet

router = DefaultRouter()
router.register(r'', StudentViewSet)

urlpatterns = router.urls