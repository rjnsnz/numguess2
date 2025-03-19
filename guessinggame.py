import random

num = random.randint(1,100)

print("Welcome to the number guessing game")
print("Im thinking of a number between 1 and 100")
print("Try to guess it, you have 5 guesses")

for i in range(5):
    guess1 = int(input("Enter your guess:"))

    if guess1 > num:
        print("The number im thinking of is smaller than" + str(guess1))
    elif guess1 < num:
        print("the number im thinking of is greater than" + str(guess1))
    else:
        print("Yes you got it right my number was" + str(num))
        break

else:
    print("Oops you lost my number was" + str(num))


