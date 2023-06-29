import sys
import random

nb = random.randint(1, 99)
# nb = 42
count = 0
# print(nb)
print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")

while 1:
    res = input("What's your guess between 1 and 99?\n")
    if res == "exit":
        sys.exit(1)
    if res.isdigit() == False:
        print("That's not a number.")
        continue
    
    count += 1
    
    if int(res) > nb:
        print("Too high!")
        continue
    elif int(res) < nb:
        print("Too low!")
        continue
    else:
        if nb == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
        if count == 1:
            # if nb == 42:
                # print("The answer to the ultimate question of life, the universe and everything is 42.")
            print("Congratulations, you've got it on your first try!")
            break
        print("Congratulations, you've got it!")
        print("You won in", count, "attempts!")
        break
        # sys.exit(1)

sys.exit(1)