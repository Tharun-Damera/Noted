from django.contrib import admin

from .models import Notes, Trash

# Register your models here.

admin.site.register(Notes)
admin.site.register(Trash)