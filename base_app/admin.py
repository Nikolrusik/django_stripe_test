from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_per_page = 5