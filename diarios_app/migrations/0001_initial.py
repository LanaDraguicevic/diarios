# Generated by Django 5.1.2 on 2024-10-15 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('pre_visualizacion', models.ImageField(blank=True, null=True, upload_to='')),
                ('localidad', models.CharField(max_length=16)),
            ],
        ),
    ]
