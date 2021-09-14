from django.contrib import admin

# Register your models here

from .models import Company,Toy

admin.site.register(Company)
admin.site.register(Toy)
