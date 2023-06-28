import sys

# creation of a dictionnary {clé: valeur}
cookbook = {
    "sandwich": {'ingredients': 'ham, bread, cheese, tomatoes', 'meal': 'lunch', 'prep_time': 10},
    "cake": {'ingredients': 'flour, sugar, eggs', 'meal': 'dessert', 'prep_time': 60},
    "salad": {'ingredients': 'avocado, arugula, tomatoes, spinach', 'meal': 'lunch', 'prep_time': 15},
}

def aff_names():
    size = len(cookbook)
    recipes = list(cookbook.keys())[:size]
    print("List of recipes in our wonderful cookbook:", recipes)

def print_recipe():
    name = input("Please enter the name of the recipe you want:\n")
    if name in cookbook:
        print("You will need", cookbook[name]['ingredients'])
        print("Eat it for", cookbook[name]['meal'])
        print("It will take you", cookbook[name]['prep_time'], "minutes")
    else:
        print("There is no recipe with that name; you can add it with option 1")

def delete_recipe():
    name = input("Please enter the name of the recipe you want to delete:\n")
    if name in cookbook:
        del cookbook[name]
    else:
        print("There is no recipe with that name")

def add_recipe():
    name = input("Please enter a name for your recipe:\n")
    ingredients = input("Please enter ingredients for your recipe:\n")
    meal = input("Please enter the type of meal for your recipe:\n")
    prep_time = input("Please enter preparation time for your recipe:\n")
    cookbook[name] = {'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time}
    print("Congrats! You just add the", name, "recipe!")


def exit_cookbook():
    print("Cookbook closed. Goodbye !")
    sys.exit(1)

def main():
    print("Welcome to the Python Cookbook !")
    print("List of available option:")
    print("	1: Add a recipe\n	2: Delete a recipe\n	3: Print a recipe\n	4: Print the cookbook\n	5: Quit")
    while 1:
        nb = input("Please select an option:\n")
        if (nb == '1'):
            add_recipe()
        elif (nb == '2'):
            delete_recipe()
        elif (nb == '3'):
            print_recipe()
        elif (nb == '4'):
            aff_names()

            # print('Ingredients list:', cookbook[nb]['ingredients'])
            
        elif (nb == '5'):
            exit_cookbook()
        else:
            print("This option doesn't exist")
    
if __name__ == "__main__":
    main()


sys.exit(1)

# cookbook contient des recettes avec :
#     > name de la recipe qui est associe a : 
#         > ingredients
#         > meal (type de repas ex lunch)
#         > prep_time (ne peut etre un nbr negatif!!!)
