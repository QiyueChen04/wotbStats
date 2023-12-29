# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Test(models.Model):
    tank_id = models.AutoField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=True)
    nation = models.TextField(blank=True, null=True)
    is_premium = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    image_preview = models.TextField(blank=True, null=True)
    image_normal = models.TextField(blank=True, null=True)
    tier = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'
