import sys

if (len(sys.argv) == 1):
	print("There is no argument")
	sys.exit(1)
if (len(sys.argv) > 2):
	print("There are too many arguments")
	sys.exit(1)

# for args in sys.argv:
    # for char in args:
sys.argv.pop(0)
# print(sys.argv)
nb = sys.argv[0]
if (nb.isdigit() == False):
	print("AssertionError: argument is not an integer")
	sys.exit(1)
if int(nb) == 0:
	print("I'm Zero")
elif (int(nb) % 2) == 0:
	print("I'm Even")
else:
	print("I'm Odd")
sys.exit(1)
    