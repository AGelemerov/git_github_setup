# ### Mathematical
# - `+`
# - `-`
# - `*`
# - `/ `
#
# ### Comparison operators
# - ` > `
# - ` < `
# - ` == `
# - ` != `
# - ` >= `
# - ` <= `

# Let's see the operators in action
a = 24
b = 16

# print(a + b)  # add the two values
# print(a - b)  # deduct b from a
# comparison
# print(a == b)
# print(a < b)
# print(a <= b)
# print(a > b)
# print(a >= b)

# % is the modulo operator, it divides the number by 2 as many times as it can and gives back the remainder

# print(270 % 30)

# != means not equal to
# it is another comparison operator
# print(1 != 2)

# Boolean built-in methods
greetings = "Hello World!"
# print(greetings)
# print(greetings.isalpha())  # checks if the string is comprised of alphabet values
# print(greetings.islower())  # checks if the string only has lower case letters
# print(greetings.startswith("H"))  # checks if the string greeting starts with a "H"
# print(greetings.endswith("!"))  # checks if the string greeting ends with a special character
# print(greetings.isdigit())

# String slicing
# String indxing - starts from 0
# Hello World!
# 01234567891011

# print(len(greetings))  # checks the length of object in brackets
# print(greetings[:5])
# print(greetings[-6:])
#
# print(greetings[0:5])
# print(greetings[6:12])

# String methods available

# use var = string "nfrowbg              "
white_space = "lots of spaces at the end          "
# print(len(white_space))

# strip() method removes white spaces at the end of the string

# print(len(white_space.strip()))
# print(len(white_space))

sample_text = "lots of text and lots more text"

# print(sample_text.count("text"))

# print(sample_text.lower())
# print(sample_text.upper())
# print(sample_text.capitalize())
# print(sample_text[-6:].upper())
# print(sample_text.replace("text", "code"))

first_name = "Angel"
last_name = "Gelemerov"
salary = 40

print(first_name)
print(last_name)
print(first_name + last_name)

print(first_name + " " + last_name)
print(first_name, last_name)

print(first_name + " " + last_name + " 1 " + str(salary))
print(first_name, last_name, salary)
print(first_name + " " + last_name + " 3 " + salary.__str__())
# F-Strings
print(f"Hello {first_name} {last_name}")  # only works with 3.6+

