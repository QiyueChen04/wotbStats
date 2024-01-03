from django.contrib import admin
from .models import Results

class compareAdmin(admin.ModelAdmin):
    list_display = ("tank_id", "name", "image_preview", "image_normal", "nation", "is_premium", "tier", "type")

admin.site.register(Results, compareAdmin)