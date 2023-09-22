from django.shortcuts import render

# Create your views here.

from applipizza.models import Pizza
from applipizza.models import Ingredient


def pizzas(request) : 

    lesPizzas = Pizza.objects.all()

    return render(
        request,
        'applipizza/pizza.html',
        {'pizzas' : lesPizzas}
    )

def ingredients(request) :

    lesIngredients = Ingredient.objects.all()

    return render(
        request,
        'applipizza/ingredients.html',
        {'ingredient' : lesIngredients}
    ) 