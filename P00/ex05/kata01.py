import sys

# creation of a dictionary :
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for keys, value in kata.items():
	print(keys, "was created by", value)

sys.exit(1)