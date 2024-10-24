from django import forms

class Busqueda(forms.Form):

    LOCALIDAD_CHOICES = [
        ('Nacional', 'Nacional'),
        ('Regional', 'Regional'),
    ]

    titulo = forms.CharField(required=False, label='Título')
    fecha_inicio = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha Inicio')
    fecha_fin = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha Fin')
    localidad = forms.ChoiceField(required=False, label='Localidad', choices=LOCALIDAD_CHOICES)


