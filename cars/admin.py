from django.contrib import admin
from cars.models import car, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',) # campo que o adm podera ver ou ajustar
    search_fields = ('name',) # como podera procurar a tabela


class carAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') # campos da tabela para cadastro de produtos 
    search_fields = ('model','brand') # como podera procurar a tabela 

admin.site.register(Brand, BrandAdmin)
admin.site.register(car, carAdmin)

