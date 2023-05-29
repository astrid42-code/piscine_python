import sys

# delete the first argv (file name)
# sys.argv.pop(0)

str = ""
for args in sys.argv[1:]:
    for char in args:
        if (char.isupper()):
            str += char.lower()
        else:
            str += char.upper()
print(str[::-1])

# Slice notation takes the form [start:stop:step]. In this case, we omit the start and stop positions since we want the whole string. We also use step = -1, which means, "repeatedly step from right to left by 1 character".