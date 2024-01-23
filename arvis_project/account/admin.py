from django.contrib import admin



# Register your models here.
from .models import *
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id","username")
    list_display_links = ("id","username")
    search_fields = ("username",)

admin.site.register(CustomUser,CustomUserAdmin)
