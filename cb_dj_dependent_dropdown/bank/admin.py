from django.contrib import admin

# Register your models here.
from bank.models import registration, confir

admin.site.register(registration)
admin.site.register(confir)
