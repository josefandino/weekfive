from django.contrib import admin
from .models import Materia



@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
   list_display = ["area", "description", "active", "credit", "name", "code"]
