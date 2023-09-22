from django.db import models

# Create your models here.

class Ingredient(models.Model):
    
    # idIngredient est une clé primaire, n auto-incrémentée => AutoField
    idIngredient = models.AutoField(primary_key=True)
    
    #nomIngredient est une chaines de caractères => CharField
    nomIngredient = models.CharField(max_length=50, verbose_name='le nom de l\'ingrédient')
    
    # une méthode de type "toString"
    def __str__(self) -> str:
        return self.nomIngredient
    
class Pizza(models.Model):
    # idPizza est une clé primaire, n auto-incrémentée => AutoField
    idPizza = models.AutoField(primary_key=True)
    
    #nomPizza est une chaines de caractères => CharField
    nomPizza = models.CharField(max_length=50, verbose_name='le nom de la pizza')
    
    #prixPizza est un nombre décimal => DecimalField
    prixPizza = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='le prix de la pizza')
    
    #une méthode de type "toString"
    def __str__(self) -> str:
        return 'pizza' + self.nomPizza + '(prix : ' + str(self.prixPizza) + '€)'
    
class Composition(models.Model) : 
    
    # la classe Meta qui gère l'unicité du couple de clés étrangères
    class Meta:
        unique_together = (('ingredient', 'pizza'),) # le nom des chaps clés étrangères
        
    # idComposition est une clé primaire, n auto-incrémentée => AutoField
    idComposition = models.AutoField(primary_key=True)
    
    # les deux champs clés étrangères, dont les noms correspondent
    # aux classe respectives, en minuscules 
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    
    # l'autre champ, chaîne de caractères 
    quantite = models.CharField(max_length=100, verbose_name='la quantité ')
    
    # une méthode de type "toString"
    def __str__(self) -> str:
        ing = self.ingredient
        piz = self.pizza
        return ing.nomIngredient + ' fait partie de la pizza ' + piz.nomPizza + '( quantité ' + self.quantite + ')'