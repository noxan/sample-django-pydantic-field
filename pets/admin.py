from django.contrib import admin

from .models import PetsModel


@admin.register(PetsModel)
class PetsModelAdmin(admin.ModelAdmin):
    pass
