# Generated by Django 4.2.8 on 2024-01-09 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extApi', '0003_alter_tanks_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tanks',
            new_name='Tank',
        ),
    ]