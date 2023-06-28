import sys
import string

if len(sys.argv) != 3:
    assert False, "ERROR: wrong number of arguments."

s = str(sys.argv[1])
try:
    n = int(sys.argv[2])
except Exception:
	assert False, "argument is not an int"

# print(s, n)
def filter():
    res = [s.translate(str.maketrans('', '', string.punctuation))]
    # print(res)
    # 1 splitter les mots (avec espace(s) comme sep)
    # 2 checker la taille de chaque mot de la liste : si len du mot >= n 
    #     recuperer le mot dans la nouvelle liste
    # 3 transformer en list comprehension 

filter()

sys.exit(1)

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# cf example : https://www.w3schools.com/python/python_lists_comprehension.asp