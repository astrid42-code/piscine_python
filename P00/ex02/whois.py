import sys

sys.argv.pop(0)

i = 0

for args in sys.argv[i:]:
    for char in args:
        nb = sys.argv[i]
        if (nb.isdigit() == False):
            print("AssertionError: argument is not an integer")
    print(nb)
    