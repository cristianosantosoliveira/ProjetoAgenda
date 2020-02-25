from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'cidade', 'categoria', 'mostrar')
    list_display_links = ('nome', 'sobrenome', 'cidade')
    search_fields = ('nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
