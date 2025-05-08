from django.contrib import admin

from sistema import models

#aqui fica o registro do usuario
@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','email','ativo') 

#aqui fica o registro do filme
@admin.register(models.film)
class filmAdmin(admin.ModelAdmin):
    list_display = ('id','nome','ano','estudio','genero', 'sinopse')
    
#aqui fica o registro do genero
@admin.register(models.genero)
class generoAdmin(admin.ModelAdmin):
    list_display = ('id','nome')