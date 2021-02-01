from django.contrib import admin
from .models import Curso, Avaliacao
# Register your models here.


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'data_publicacao', 'data_atualizacao', 'ativo')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email','avaliacao', 'data_atualizacao', 'data_publicacao','ativo')