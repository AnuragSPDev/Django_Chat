from django.contrib import admin
from .models import Rooms

# Register your models here.
@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug_field']