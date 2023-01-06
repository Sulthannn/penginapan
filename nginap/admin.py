from django.contrib import admin
from .models import *


class penginapanadmin(admin.ModelAdmin):
    list_display = ['koordinat', 'nama', 'harga', 'lokasi', 'tersisa']
    search_fields = ['koordinat', 'jenis_id']
    list_filter = ['jenis_id']
    list_per_page = 5

# Register your models here.
admin.site.register(Penginapan, penginapanadmin)
admin.site.register(Jenis)