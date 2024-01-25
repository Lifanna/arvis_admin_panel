from django.contrib import admin
from .models import *
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id","username")
    list_display_links = ("id","username")
    search_fields = ("username",)

admin.site.register(CustomUser,CustomUserAdmin)
