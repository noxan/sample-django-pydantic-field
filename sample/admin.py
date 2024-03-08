from django.contrib import admin

from sample.models import SampleModel


@admin.register(SampleModel)
class SampleAdmin(admin.ModelAdmin):
    pass
