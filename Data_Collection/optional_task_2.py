# Create a little program that ask the user for the following details:
# - name
# - height
# - favourite_color
# - secrete_spirit_animal
#
# Then:
# Capture these inputs Print a tailored welcome message to the user
# print other details gathered, except the secret of course print the first and last letter of the secrete_spirit_animal
# * print the number of characters the secrete_spirit_animal
#
# hint, think about casting your data type.

"""
----------------SOLUTION------------------
"""
import re

name = input("Please enter your name")
height = input("Please enter you height (ft)")
favourite_colour = input("Please enter your favourite colour")
secret_spirit_animal = input("Please enter your secret spirit animal 👀")

print(f"Hello {name} your favourite colour is {favourite_colour} and you are {height}ft tall")
print(f"Your secret spirit animal has {len(secret_spirit_animal)} amount of letters")
print("Your secret animal is: {f}{s}{t}".format(f=secret_spirit_animal[0],
                                                s=re.sub('[A-Z|a-z]', '*', secret_spirit_animal[1:-1]),
                                                t=secret_spirit_animal[-1]))
