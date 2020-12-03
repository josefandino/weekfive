from rest_framework import serializers

from .models import Teacher

class TeacherSerializers(serializers.ModelSerializer):
   class Meta:
      model = Teacher
      fields = ['id','name','last_name','phone','email','active']
