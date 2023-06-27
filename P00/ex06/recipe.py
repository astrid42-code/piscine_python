import sys

# creation of a dictionnary {clé: valeur}
cookbook = {
    'sandwich': {'ingredients': 'ham, bread, cheese, tomatoes', 'meal': 'lunch', 'prep_time': 10},
    'cake': {'ingredients': 'flour, sugar, eggs', 'meal': 'dessert', 'prep_time': 60},
    'salad': {'ingredients': 'avocado, arugula, tomatoes, spinach', 'meal': 'lunch', 'prep_time': 15},
}

for keys in cookbook.items():
    # for keys in sandwich.items():
    print(keys)
    # print(values)

sys.exit(1)

# cookbook contient des recettes avec :
#     > name de la recipe qui est associe a : 
#         > ingredients
#         > meal (type de repas ex lunch)
#         > prep_time (ne peut etre un nbr negatif!!!)

# dans fct pour ajouter une recette avec input user penser a demander un nbr positif only (a check dans parsing)