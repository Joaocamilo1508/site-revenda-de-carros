from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 200)
    
    def __str__(self):
        return self.name

class car(models.Model): # criando uma tabela com o nome car
    id = models.AutoField(primary_key=True) # aqui cria um iD para cada produto cadastrado 
    model = models.CharField(max_length=200) # modelo do produto com no maximo 200 caracteres 
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name= 'car_brand') # marca do produto com a lista de produto ja  existente para escolher
    factory_year = models.IntegerField(blank=True, null=True) # ano de fabricação do produto 
    model_year = models.IntegerField(blank=True, null=True) # ano do modelo do produto 
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True) # valor do produto 
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    

    def __str__(self):
        return self.model

