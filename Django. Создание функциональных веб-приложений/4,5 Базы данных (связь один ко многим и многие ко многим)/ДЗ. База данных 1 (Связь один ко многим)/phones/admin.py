from django.contrib import admin
from .models import Phone


# Register your models here
class PhoneAdmin(admin.ModelAdmin): # добавляет админку
    pass


admin.site.register(Phone, PhoneAdmin)

