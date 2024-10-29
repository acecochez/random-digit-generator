# RANDOM NUMBER GENERATOR

# Importing sample
from random import sample

# Number list
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Spacing line
def sp():
    print("-" * 35)

# Amount of digits
def numgen():
    print("\nGenerate random digits")
    digits = input("Type a number up to 5: ")
    for num in digits:

        # Generate 1 digit
        if digits == "1":
            print("\nYour", digits, "randomized digit is:")
            print(sample(nums, k=1))
            sp()
            numgen()
            break

        # Generate 2 digits
        if digits == "2":
            print("\nYour", digits, "randomized digits are:")
            print(sample(nums, k=2))
            sp()
            numgen()
            break

        # Generate 3 digits
        if digits == "3":
            print("\nYour", digits, "randomized digits are:")
            print(sample(nums, k=3))
            sp()
            numgen()
            break
        
        # Generate 4 digits
        if digits == "4":
            print("\nYour", digits, "randomized digits are:")
            print(sample(nums, k=4))
            sp()
            numgen()
            break

        # Generate 5 digits
        if digits == "5":
            print("\nYour", digits, "randomized digits are:")
            print(sample(nums, k=5))
            sp()
            numgen()
            break

        # Invalid input   
        else:
            print("\nInvalid input! Try again.")
            sp()
            numgen()
            break

# Launch
sp()
print("Welcome to the random number generator!")
sp()
numgen()
