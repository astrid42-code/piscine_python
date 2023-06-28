import sys

if len(sys.argv) < 3:
	print("Usage: python operations.py <number1> <number2>\nExample:\npython operations.py 10 3")
	sys.exit(1)
elif len(sys.argv) > 3:
	assert False, "too many arguments"

try:
	nb1 = int(sys.argv[1])
	nb2 = int(sys.argv[2])
except Exception:
	assert False, "argument is not an integer"

def aff(nb1, nb2):
	print("Sum:		", nb1 + nb2)
	print("Difference:	", nb1 - nb2)
	print("Product:	", nb1 * nb2)
	if nb2 == 0:
		print("Quotient: 	 ERROR (division by zero)")
		print("Remainder: 	 ERROR (modulo by zero)")
		sys.exit(1)
	print("Quotient:	", nb1 / nb2)
	print("Remainder:	", nb1 % nb2)

aff(nb1, nb2)

sys.exit(1)