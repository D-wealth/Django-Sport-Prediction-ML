from django.contrib import admin
from . import models

# Register your models here.


class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'age', 'sex', 'predictions')

admin.site.register(models.Data, DataAdmin)
