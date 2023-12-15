"""
URL configuration for webpizza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from applipizza import views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    #Pour les pizzas
    path('pizzas/', views.pizzas),
    path('pizza/<int:pizza_id>/', views.pizza),
    path('pizza/add/', views.formulaireCreationPizza),
    path('pizza/traitement', views.creerPizza),
    path('pizza/<int:pizza_id>/addIngredient', views.ajouterIngredientsDansPizza),
    path('pizza/<int:pizza_id>/delete/', views.supprimerPizza),

    #Pour les Ingredients
    path('ingredients/', views.ingredients),
    path('ingredient/add/', views.formulaireCreationIngredient),
    path('ingredient/traitement', views.traitementIngredient),
    
    
]
