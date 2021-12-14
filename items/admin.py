from django.contrib import admin
from .models import Item

# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','description','enrolled_at','updated_at','price','entry_clerk']