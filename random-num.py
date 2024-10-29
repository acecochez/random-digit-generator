# RANDOM NUMBER GENERATOR
import random
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
def sp():
    print("-" * 35)

def numbergenerator():
    print("\nGenerate random digits")
    digits = input("Type a number up to 5: ")
    for num in digits:
        if digits == "1":
            print("\nYour", digits, "randomized digit is:")
            print(random.sample(numbers, k=1))
            sp()
            numbergenerator()
            break

        if digits == "2":
            print("\nYour", digits, "randomized digits are:")
            print(random.sample(numbers, k=2))
            sp()
            numbergenerator()
            break

        if digits == "3":
            print("\nYour", digits, "randomized digits are:")
            print(random.sample(numbers, k=3))
            sp()
            numbergenerator()
            break

        if digits == "4":
            print("\nYour", digits, "randomized digits are:")
            print(random.sample(numbers, k=4))
            sp()
            numbergenerator()
            break

        if digits == "5":
            print("\nYour", digits, "randomized digits are:")
            print(random.sample(numbers, k=5))
            sp()
            numbergenerator()
            break
                  
        else:
            print("\nInvalid input! Try again.")
            sp()
            numbergenerator()
            break

sp()
print("Welcome to the random number generator!")
sp()
numbergenerator()
