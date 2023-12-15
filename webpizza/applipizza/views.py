from django.shortcuts import render

# Create your views here.

from applipizza.models import Pizza
from applipizza.models import Ingredient
from applipizza.models import Composition
from applipizza.forms import IngredientForm
from applipizza.forms import PizzaForm
from applipizza.forms import CompositionForm




def pizzas(request) : 

    lesPizzas = Pizza.objects.all()

    return render(
        request,
        'applipizza/pizzas.html',
        {'pizzas' : lesPizzas}
    )

def ingredients(request) :

    lesIngredients = Ingredient.objects.all()

    return render(
        request,
        'applipizza/ingredients.html',
        {'ingredients' : lesIngredients}
    ) 
  
def pizza(request, pizza_id) :
    
    laPizza = Pizza.objects.get(idPizza=pizza_id)
    compo = Composition.objects.filter(pizza=pizza_id)
    
    #creation d'une liste des ingredients de la pizza avec leur quantité
    liste = []
    for c in compo :
        liste.append({"name" : c.ingredient.nomIngredient,"quantite" : c.quantite})
    
    listeIngredients = []
    listeIngredients = [{'id': compo.idComposition, 'name': compo.ingredient.nomIngredient, 'quantity': compo.quantite} for compo in compo]
    
    
    return render(
        request,
        'applipizza/pizza.html',
        {'pizza' : laPizza, 'compo' : liste, "lesIng" : listeIngredients},
    )


def formulaireCreationIngredient(request) : 
    return render(
        request,
        'applipizza/formulaireCreationIngredient.html',
    )
    
def traitementIngredient(request):

    form = IngredientForm(request.POST)    
    if form.is_valid():
        nomIng = form.cleaned_data['nomIngredient']
        ing = Ingredient()
        ing.nomIngredient = nomIng
        ing.save()
        
    return render(
        request,
        'applipizza/traitementIngredient.html',
    )   
    
    
def formulaireCreationPizza(request) : 
    return render(
        request,
        'applipizza/formulaireCreationPizza.html',
    )

def creerPizza(request):

    form = PizzaForm(request.POST)
    nomPizza = ""
    prixPizza = ""
    
    if form.is_valid():
        
        nomPizza = form.cleaned_data['nomPizza' ]
        prixPizza = form.cleaned_data['prixPizza' ]

        piz = Pizza()
        piz.nomPizza = nomPizza
        piz.prixPizza = prixPizza
        piz.save()
        
        
    return render(
        request,
        'applipizza/traitementPizza.html',
        {"nomPizza" : nomPizza, "prixPizza" : prixPizza}
    )
    
"""
def ajouterIngredientsDansPizza(request, pizza_id) : 
    ing = ""
    qte = ""
    piz = ""
    
    # récupération du formulaire posté
    formulaire = CompositionForm(request.POST)
    
    if formulaire.is_valid() :
        # récupération des données postées
        lesIngredientsDeLaPizza = ((ligne.ingredient) for ligne in compoPizza)

        ing = formulaire.cleaned_data['ingredient'] #ajouter
        qte = formulaire.cleaned_data['quantite'] #ajouter
        piz = Pizza.objects.get(idPizza = pizza_id) #ajouter
        compoPizza = Composition.objects.filter(pizza = pizza_id) #ajouter
        lesIngredientsDeLaPizza = ((ligne.ingredient) for ligne in compoPizza) #ajouter
        
        
        if ing in lesIngredientsDeLaPizza :
            compo = Composition.objects. filter(pizza = pizza_id, ingredient = ing)
            compo.delete ()
            
        # création de la nouvelle instance de Composition et remplissage des attributs
        compo = Composition()
        compo.ingredient = ing
        compo.pizza = piz
        compo.quantite = qte
        
        
        # sauvegarde dans la base de la composition
        compo.save ()
        
    # récupération de tous les ingrédients pour construire le futur select
    lesIngredients = Ingredient.objects.all()

    # actualisation des ingrédients entrant dans la composition de la pizza
    compoPizza = Composition.objects.filter(pizza = pizza_id)

    # on crée une liste dont chaque item contiendra 'identifiant de la composition (idComposition), # le nom de l'ingrédient et la quantité de 'ingrédient dans cette composition
    listeIngredients = []
    
     # Le nom de l'ingrédient et la quantité de l'ingrédient dans cette composition
    listeIngredients = []
    listeIngredients = [{'idComposition': compo.idComposition, 'nom': compo.ingredient.nomIngredient, 'qte': compo.quantite} for compo in compoPizza]
    

    for ligneCompo in compoPizza :
    # on récupère 1'Ingredient pour utiliser son nomIngredient
        ingredient = Ingredient.objects.get(idIngredient = ligneCompo.ingredient.idIngredient)
        listeIngredients.append({"idComposition" : ligneCompo.idComposition, 
                                 "nom" : ingredient.nomIngredient, 
                                 "qte" : ligneCompo.quantite})
    return render(
        request,
        'applipizza/pizza.html',
        {"pizza" : piz, "liste" : listeIngredients, "lesIng" : lesIngredients}
    )


def ajouterIngredientsDansPizza(request, pizza_id):
    ing = ""
    qte = ""
    piz = ""

    # récupération du formulaire posté
    formulaire = CompositionForm(request.POST)

    if formulaire.is_valid():
        # récupération des données postées
        ing = formulaire.cleaned_data['ingredient']
        qte = formulaire.cleaned_data['quantite']
        piz = Pizza.objects.get(idPizza=pizza_id)
        compoPizza = Composition.objects.filter(pizza=pizza_id)
        lesIngredientsDeLaPizza = [ligne.ingredient for ligne in compoPizza]

        if ing in lesIngredientsDeLaPizza:
            compo = Composition.objects.filter(pizza=pizza_id, ingredient=ing)
            compo.delete()

        # création de la nouvelle instance de Composition et remplissage des attributs
        compo = Composition()
        compo.ingredient = ing
        compo.pizza = piz
        compo.quantite = qte

        # sauvegarde dans la base de la composition
        compo.save()

    # récupération de tous les ingrédients pour construire le futur select
    lesIngredients = Ingredient.objects.all()

    # actualisation des ingrédients entrant dans la composition de la pizza
    compoPizza = Composition.objects.filter(pizza=pizza_id)

    # on crée une liste dont chaque item contiendra 'identifiant de la composition (idComposition),
    # le nom de l'ingrédient et la quantité de l'ingrédient dans cette composition
    listeIngredients = []

    for ligneCompo in compoPizza:
        # on récupère l'Ingredient pour utiliser son nomIngredient
        ingredient = Ingredient.objects.get(idIngredient=ligneCompo.ingredient.idIngredient)
        listeIngredients.append({
            "idComposition": ligneCompo.idComposition,
            "nom": ingredient.nomIngredient,
            "qte": ligneCompo.quantite
        })

    return render(
        request,
        'applipizza/pizza.html',
        {"pizza": piz, "liste": listeIngredients, "lesIng": lesIngredients}
    )

"""

def ajouterIngredientsDansPizza(request, pizza_id) :
    # Récupération du formulaire posté
    formulaire = CompositionForm(request.POST)
    ing = ""
    qte = ""
    piz = ""
    
    if formulaire.is_valid() :
        # récupération des données postées
        ing = formulaire.cleaned_data['ingredient']
        qte = formulaire.cleaned_data['quantite']
        piz = Pizza.objects.get(idPizza = pizza_id)
        compoPizza = Composition.objects.filter(pizza = pizza_id)
        lesIngredientsDeLaPizza = ((ligne.ingredient) for ligne in compoPizza)
        
        if ing in lesIngredientsDeLaPizza :
            compo = Composition.objects.filter(pizza = pizza_id, ingredient = ing)
            compo.delete()
            
        # Création de la nouvelle instance de composition et remplissage des attributs
        compo = Composition()
        compo.ingredient = ing
        compo.pizza = piz
        compo.quantite = qte
        # Sauvegarde dans la base de la composition 
        compo.save()
        
    # Récupération de tous les ingrédients pour construire le futur select
    lesIngredients = Ingredient.objects.all()
    # Actualisation des ingrédients entrant dans la composition de la pizza
    compoPizza = Composition.objects.filter(pizza = pizza_id)
    # On crée une liste dont chaque item contiendra l'identifiant de la composition (idComposition).
    # Le nom de l'ingrédient et la quantité de l'ingrédient dans cette composition
    listeIngredients = []
    listeIngredients = [{'id': compo.idComposition, 'name': compo.ingredient.nomIngredient, 'quantity': compo.quantite} for compo in compoPizza]
    

    # O@n retourne l'emplacement du template, la pizza récupérée et la liste des ingrédients calculé ci-dessus
    return render(
        request,
        'applipizza/pizzas.html',
        {"pizza" : piz, "lesIng" : listeIngredients, "all_ingredients" : lesIngredients}
    )
    
    """
    Créez la view supprimerPizza(request, pizza_id) dans le fichier views.py. Cette vue devra :
a. récupérer la pizza à supprimer (grâce à la méthode get),
b. appeler la méthode delete() sur cette pizza,
c. récupérer la liste de toutes les pizzas grâce à la méthode all() comme dans la vue pizzas,
d. appeler le template pizzas.html en lui fournissant le liste des pizzas (comme dans la vue pizzas).
    """

def supprimerPizza(request, pizza_id):
    # Récupération de la pizza à supprimer
    piz = Pizza.objects.get(idPizza=pizza_id)
    # Suppression de la pizza
    piz.delete()
    # Récupération de la liste de toutes les pizzas
    lesPizzas = Pizza.objects.all()
    # Retour à la page pizzas.html
    return render(
        request,
        'applipizza/pizzas.html',
        {'pizzas': lesPizzas}
    )