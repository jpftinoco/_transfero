from django.utils import timezone
from django.db import models

# aqui vai ficar a lass modelo do usuario
# nome,sobrenome,cpf,gmail,endereço,foto
#data_cadastro,ativo
class Usuario(models.Model):
    nome = models.CharField(max_length = 50)
    sobrenome = models.CharField(max_length = 50)
    cpf = models.CharField(max_length = 11)
    telefone = models.CharField(max_length = 20)
    email = models.EmailField()
    endereco = models.CharField(max_length = 100)
    data_cadastro= models.DateField(default= timezone.now)
    ativo = models.BooleanField(default = True)
    def __str__(self):
        return f'{self.nome} {self.sobrenome} seja bem vindo meu cria'

class film(models.Model):
    nome = models.CharField(max_length = 100)
    ano = models.DateField()
    estudio = models.CharField(max_length = 20)
    genero = models.CharField(max_length = 50)
    sinopse = models.CharField(max_length = 300)
    data_lançamento = models.DateField()

    def __str__(self):
        return self.nome

class genero(models.Model):
    nome = models.CharField(max_length = 20)
    data = models.DateField()

    def __str__(self):
        return self.nome
    