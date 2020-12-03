# from profesores.views import Teacher
# from django.urls import path

# urlpattern = [
#     path('', teacher),
#     path('<teacher_id>/', teacher),
# ]

from rest_framework.routers import DefaultRouter

from .views import TeacherViewSet

router = DefaultRouter()
router.register(r'', TeacherViewSet)

urlpatterns = router.urls