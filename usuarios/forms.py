from django import forms
from sistema.models import Usuario

class Usuarioform(forms.ModelForm):
    model = Usuario
    fields = ['nome','sobrenome','cfp','telefone','email','endereço','imagem',]
    
