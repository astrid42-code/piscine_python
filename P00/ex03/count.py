import sys

# Create a function called text_analyzer that takes a single string argument and displays
# the sums of its upper-case characters, lower-case characters, punctuation characters and
# spaces.
# • If None or nothing is provided, the user is prompted to provide a string.
# • If the argument is not a string, print an error message.
# • This function must have a docstring explaning its behavior.
# Test your function with the python console

# Docstrings act as documentation for the class, module, and packages.
# On the other hand, Comments are mainly used to explain non-obvious portions
#  of the code and can be useful for comments on Fixing bugs and tasks 
#  that are needed to be done.

# 3 cas d erreurs + sortie
# 1 creer une fonction text_analyser(string str)
# 2 sum(str.isupper() + str.islower() + str.is?? + str.isspace())

def text_analyser(str):

    """
    This function takes a single string argument and displays
    the sums of its upper-case characters, lower-case characters, 
    punctuation characters and spaces.
    Then it prints each category
    """

    if 

    int i = 0
    int res
    int uc = 0
    int lc = 0
    int p = 0
    int s = 0

    if str:
        while str[i]:
            if str[i].isupper():
                uc += 1
            elif str[i].islower():
                lc += 1
            elif str[i].isspace():
                s += 1
            elif str[i] > 32 and str[i] < 58:
                p += 1
            i += 1

    res = sum(uc + lc + p + s)
    print(res)

def aff():
    print("from " )

sys.exit(1)