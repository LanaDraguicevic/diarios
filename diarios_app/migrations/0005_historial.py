# Generated by Django 5.1.2 on 2024-10-25 23:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diarios_app', '0004_alter_diarios_pre_visualizacion'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_visita', models.DateTimeField(auto_now_add=True)),
                ('diario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diarios_app.diarios')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
