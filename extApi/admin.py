from django.contrib import admin

from .models import Tanks

class extAdmin(admin.ModelAdmin):
    list_display = ("tank_id", "name", "image_preview", "image_normal", "nation", "is_premium", "tier", "type")

admin.site.register(Tanks, extAdmin)
