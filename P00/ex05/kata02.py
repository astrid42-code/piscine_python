import sys

# creation of a tuple :
kata = (2019, 9, 25, 3, 30)
month = kata[1]
day = kata[2]
year = kata[0]
hour = kata[3]
minute = kata[4]
sep1 = "/"
sep2 = ":"
sep3 = " "


# print(kata[1],"/", kata[2], "/", kata[0], kata[3], ":", kata[4])
print(month, sep1, day, sep1, year, sep3, hour, sep2, minute, sep="")

sys.exit(1)

# resultat attendu :
# $> python3 kata02.py | cat -e
# 09/25/2019 03:30$
# $> python3 kata02.py | wc -c
# 17
# $
# > ok pour l'affichage mais pas pour le resultat en wc -c (15 au lieu de 17)