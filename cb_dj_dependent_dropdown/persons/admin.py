from django.contrib import admin

# Register your models here.
from persons.models import Person, District, Branch

admin.site.register(Branch)
admin.site.register(District)
admin.site.register(Person)
