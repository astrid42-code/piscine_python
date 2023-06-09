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

def text_analyzer(str):

    """
    This function takes a single string argument and displays
    the sums of its upper-case characters, lower-case characters, 
    punctuation characters and spaces.
    Then it prints each category
    """

    if len(str) == 0:
        main()

    uc = 0
    lc = 0
    s = 0
    nb = 0
    if len(str) > 0:
        for i in str:
            if i.isupper():
                uc += 1
            elif i.islower():
                lc += 1
            elif i.isspace():
                s += 1
            elif i.isdigit(): 
                nb += 1
        total = len(str)
        # p : punctuation = nb total de chars - analyzed chars - numbers
        p = total - (uc + lc + s) - nb
        aff(total, uc, lc, p, s)

def aff(total, uc, lc, p, s):
    print("The text contains ", total, " character(s):")
    print("- ", uc, " upper letter(s)")
    print("- ", lc, " lower letter(s)")
    print("- ", p, " punctuation mark(s)")
    print("- ", s, " space(s)")

def main():
    if (len(sys.argv) > 1):
        assert False, "ERROR: wrong number of arguments."
    # pb entre le sujet et lexemple donne (avec argument a analyser...)
    text = input("What is the text to analyze?\n")
    try:
        text_analyzer(text)
    except Exception:
	    assert False, "AssertionError: argument is not a string"
    # ne prend pas l exception : comment verifier le type du txt avant de l envoyer?

if __name__ == "__main__":
    main()

# sys.exit(1)


# plutot fonctionnel mais cetains exemples du sujet ne sont pas ok :
# >>> text_analyzer()
# What is the text to analyze?
# >>> text_analyzer(42)
# AssertionError: argument is not a string
# > a priori meme souci de nonprise en compte directement dans la console de ma fonction
