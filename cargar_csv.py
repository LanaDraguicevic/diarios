import csv
import os
import django
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diariosproject.settings")
django.setup()

from diarios_app.models import Diarios

archivo_csv= "C:/Users/Sladjana/Desktop/diarios,fecha,localidad,codigo1.csv"

with open(archivo_csv, newline= '', encoding='ISO-8859-1') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for fila in reader:

        nombre = fila['diarios']
        fecha = datetime.strptime(fila['fecha'], "%d-%m-%Y").date()
        localidad = fila['localidad']
        codigo = fila['codigo']

        Diarios.objects.create(nombre=nombre, fecha=fecha, localidad=localidad, cod=codigo)
