import sys
import string

if len(sys.argv) != 3:
    assert False, "ERROR: wrong number of arguments."

s = str(sys.argv[1])
try:
    n = int(sys.argv[2])
except Exception:
	assert False, "argument is not an int"

# print(s, n)
def filter():
    res = [s.translate(str.maketrans('', '', string.punctuation))]
    print("1=", res)
    res = ''.join(res)
    print("2=",res)
    x = res.split()
    # list comprehension
    newlist = [words for words in x if len(words) > n]
    print(newlist)


filter()

sys.exit(1)

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# cf example : https://www.w3schools.com/python/python_lists_comprehension.asp


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#     print(x)
#     if "a" in x:
#         newlist.append(x)

# print(newlist)