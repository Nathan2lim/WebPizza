from django.db import models

# Create your models here.

class Ingredient(models.Model):
    
    #clé primaire avec auto incrémentation
    idIngredient = models.AutoField(primary_key=True)

    #nom de l'ingrédient
    nomIngredient = models.CharField(max_length=50, verbose_name= "Nom de l'ingrédient")

    #methode to string
    def __str__(self):
        return self.nomIngredient

class Pizza(models.Model) :

    #clé primaire avec auto incrémentation
    idPizza = models.AutoField(primary_key=True)

    #nom de la pizza
    nomPizza = models.CharField(max_length=50, verbose_name= "Nom de la pizza")

    #prix de la pizza
    prixPizza = models.FloatField(max_digits=4, decimal_places=2, verbose_name= "Prix de la pizza")

    #tosring
    def __str__(self):
        return self.nomPizza


