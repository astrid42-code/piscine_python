import sys

# creation of a tupple
kata = (0, 4, 132.42222, 10000, 12345.67)
zero = kata[0]
four = kata[1]
float_nb = '{:.2f}'.format(kata[2])
thousand = '{:.2e}'.format(kata[3])
other_float = '{:.2e}'.format(kata[4])
sep = ""

print(f"module_", zero, zero, ", ex_", zero, four, " : ", float_nb, ", ", thousand, ", ", other_float, sep="" )


sys.exit(1)

# resultat attendu :
# $> python3 kata04.py
# module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
# $> python3 kata04.py | cut -c 10,18
# ,:

# doc :
# https://python.sdv.univ-paris-diderot.fr/03_affichage/