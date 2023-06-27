import sys

# creation of a tuple :
kata = (2019, 9, 25, 3, 30)
month = kata[1]
day = kata[2]
year = kata[0]
hour = kata[3]
minute = kata[4]
zero = 0
sep1 = "/"
sep2 = ":"
sep3 = " "

print(zero, month, sep1, day, sep1, year, sep3, zero, hour, sep2, minute, sep="")

sys.exit(1)