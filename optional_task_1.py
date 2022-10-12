# # User story 1 ## As a user, I want to be able to guess a number and know if i got it correct or not, so that I can
# know if I won or not.

# We should define/assign number to a variable called magic_number --> might be cool to use the py library random
# magic_number =

# I need to ask user for input


# I need to check if this input matches a magic_number


# I need to let the user know if the response was correct or not
# self five

"""
-----------SOLUTION------------
"""
import random as r

# 1
randint = r.randint(0, 100)

while True:
    magic_number = int(input("Guess a number between 0 and 100: "))
    if randint == magic_number:
        print("Congratulations, you guessed the number!")
        break

    elif randint < magic_number:
        print("Too big!\n")

    elif randint > magic_number:
        print("Too small!\n")
