# Generated by Django 5.1.3 on 2024-12-03 04:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diarios_app', '0006_diariodisponibilidad_diarios_disponibilidad'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='historial',
            unique_together={('usuario', 'diario')},
        ),
        migrations.CreateModel(
            name='DiarioSolicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('devuelto', models.BooleanField(default=False)),
                ('diario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diarios_app.diarios')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('diario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diarios_app.diarios')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
