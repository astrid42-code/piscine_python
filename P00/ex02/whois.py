import sys

if (len(sys.argv) == 1):
	print("There is no argument")
	sys.exit(1)
if (len(sys.argv) > 2):
	assert False, "There are too many arguments"
	# print("Assertion error: there are too many arguments")
	# sys.exit(1)

sys.argv.pop(0)

try:
	nb = int(sys.argv[0])
except Exception:
	assert False, "argument is not an integer"

if nb == 0:
	print("I'm Zero")
elif nb % 2 == 0:
	print("I'm Even")
else:
	print("I'm Odd")

sys.exit(1)
