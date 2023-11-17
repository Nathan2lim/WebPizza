from django import forms
from django.forms import ModelForm
from applipizza.models import Ingredient
from applipizza.models import Pizza
from applipizza.models import Composition



# class ingredientForm qui herite de ModelForm
class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['nomIngredient']

# class ingredientForm qui herite de ModelForm
class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['nomPizza', 'prixPizza']


#Dans le fichier forms.py, créez une nouvelle classe de formulaire ,son nom est CompositionForm, il hérite de ModelForm
class CompositionForm(ModelForm):
    class Meta:
        model = Composition
        fields = ['ingredient', 'quantite']
