## COMANDOS PRINCIPAIS DO DJANGO

1. Para criar um ambiente virtual -> `python -m venv venv`

2. No Windows, para ativar o ambiente virtual utilizamos \. Ex: `venv\Scripts\activate`

3. Para instalar o django no projeto -> `pip install django`

4. Para criar um projeto Django -> `django-admin startproject project .`

5. Para subir o servidor, utilizamos -> `python manage.py runserver`

6. Para criar um novo APP -> `python manage.py startapp home`

7. Para realizar a coleta dos arquivos estáticos -> `python manage.py collectstatic`

8. Para desativar a venv no projeto django -> `deactivate`

## Ações das migrações
1. Para preparar as migrações -> `python manage.py makemigrations`
2. Para realizar as migrações -> `python manage.py migrate`


## Criando e modificando a senha do super usuário Django
1. Para criar o superuser -> `python manage.py createsuperuser`
2. Para alterar a senha, caso você esqueça -> `python manage.py changepassword nomedousuario`


=> Documentações
https://docs.djangoproject.com/en/5.1/topics/templates/
https://www.w3schools.com/django/django_urls.php

=> Comando quando for instalar o django pela primeira vez no computador
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
