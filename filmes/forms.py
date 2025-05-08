from django import forms
from sistema.models import film

class filmForm(forms.ModelForm):
    class Meta:
        model = film
        fields = ['nome', 'ano', 'estudio', 'genero', 'data_lançamento', 'sinopse',]