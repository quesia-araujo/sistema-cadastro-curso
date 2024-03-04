from django.contrib import admin
from base.models import Cadastro
# Register your models here.

# Registrando modelos que quero que apareçam no painel administrativo
@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome','email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']
