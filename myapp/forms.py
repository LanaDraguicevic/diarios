from django import forms


edits = [
	('0', 'La Nacion'),
	('1', 'El Mercurio'),
    ('2', 'La Tercera'),
    ('3', 'La Cuarta'),
    ]

meses = [
	('0', 'Enero'),
	('1', 'Febrero'),
    ('2', 'Marzo'),
    ('3', 'Abril'),
    ('4', 'Mayo'),
	('5', 'Junio'),
	('6', 'Julio'),
	('7', 'Agosto'),
	('8', 'Septiembre'),
	('9', 'Octubre'),
	('10', 'Noviembre'),
	('11', 'Diciembre'),      
	]


class ProductForm(forms.Form):

	Editorial = forms.FloatField(label='Editorial del diario', widget=forms.Select(choices=edits), required = True)
	Día = forms.FloatField(label='Dia en que se publico el diario',min_value=1,max_value=31, required = True)	
	Mes = forms.FloatField(label='Mes en que se publico el diario', widget=forms.Select(choices=meses), required = True)
	Año = forms.FloatField(label='Año de publicacion', min_value=1812,max_value=2024, required = True)
	
