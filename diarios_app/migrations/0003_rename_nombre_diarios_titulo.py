# Generated by Django 5.1.2 on 2024-10-24 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diarios_app', '0002_diarios_cod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diarios',
            old_name='nombre',
            new_name='titulo',
        ),
    ]
