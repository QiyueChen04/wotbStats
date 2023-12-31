from django.db import models

# Create your models here.
class Tanks(models.Model):
    tank_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=255, blank = True, null = True)
    image_preview = models.CharField(max_length=255, blank = True, null = True)
    image_normal = models.CharField(max_length=255, blank = True, null = True)
    nation = models.CharField(max_length = 255, blank = True, null = True)
    is_premium = models.IntegerField(blank = True, null = True)
    tier = models.IntegerField(blank = True, null = True)
    type = models.CharField(max_length=255, blank = True, null = True)
    