# initial coding exercise
# What is Python and how to code in i

# Dynamically typed language
# Python variables
# We use variables to store data
# To store user data - hard code data - any other type
# first_name = "Angel" - String/str
# last_name = "Gelemerov"
"""
DOB = 99 - Integer/int
UK resident = yes/no - Boolean/bool
salary = 40000 - Integer/int
travel = 15.4 - Float/float
gross_salary = "salary + travel"
"""
#
# first_name = "Angel"
# last_name = "Gelemerov"
# salary = 50
# travel = 0.5
#
# # print("Angel")
# print(first_name)
# print(last_name)
# print(salary)
# print(travel)
#
# # how to find out the type of the data stored in the variable
# print(type(salary))
#
# print("Good Morning, please enter your name")
#
# name = input()
# print(name)
# print("Hello " + name)


# first_name = input("Please enter your first name. ")
# last_name = input("Please enter your last name. ")
# DOB = input("Please enter your date of birth (dd/mm/yyyy). ")
# course_name = input("Please enter your course name. ")
# UK_resident = input("Are you a UK resident? ")


# print("Hello " + first_name + " " + last_name)
# print("Date of birth: " + DOB)
# print("Course name is: " + course_name)
# print("Answer to: Are you a UK resident: " + UK_resident)

first_name = input("Please enter your first name. ").capitalize()
last_name = input("Please enter your last name. ").capitalize()
DOB = input("Please enter your date of birth (dd/mm/yyyy). ")
house_num = int(input("Please enter your house number. "))
postcode = input("Please enter your postcode. ").upper()
course_name = input("Please enter your course name. ").lower().capitalize()

UK_resident = input("You are a UK resident. (True of False). ")
UK_resident = UK_resident.lower().capitalize()
UK_resident = bool(UK_resident)

print(f"Hello {first_name} {last_name}")
print(f"Date of birth: {DOB}")
print(f"Your address is: {house_num} {postcode}")
print(f"Course name is: {course_name}")
print(f"Answer to: Are you a UK resident: {UK_resident}")
