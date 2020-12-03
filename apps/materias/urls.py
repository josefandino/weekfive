# from .views import Materia
# from django.urls import path

# urlpattern = [
#     path('', materia),
#     path('<materia>/', materia)
# ]

from rest_framework.routers import DefaultRouter

from .views import MateriaViewSet

router = DefaultRouter()
router.register(r'', MateriaViewSet)

urlpatterns = router.urls