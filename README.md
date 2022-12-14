# Python Introduction

## Why Python

- Python is a dynamically typed language
- Easy to understand
- Easy to follow logic

<img src="../images/why_python.png" title="Why choose Python" alt="DevOps_Cycle" width="600"/>

## Python use cases

1. Data Analysis
2. Web Development
3. DevOps
4. Web Scrapers programming
5. Machine Learning
6. Educational
7. Software Testing

<img src="../images/python_use_cases.jpg" title="Use Cases" alt="DevOps_Cycle" width="600"/>

## Python set up with PyCharm

- Ensure you have Python version 3.7+ installed
- Install PyCharm (remember to check the box with "Add Python to PATH")
- To ensure everything is set up correctly, write a simple "hello world" command
-

## Python variables

- Variables are something we store data in
- This data can be of many types including

### Data Types

- String (str)
- Integer (int)
- Float (float) (stands for floating point number, meaning decimal point)
- Boolean (bool)
- Character (char)
- List (list)
- Etc.

- `print("Hello World")`

```python
# TASK
first_name = input("Please enter your first name. ")
last_name = input("Please enter your last name. ")
DOB = input("Please enter your date of birth (dd/mm/yyyy). ")
course_name = input("Please enter your course name. ")
UK_resident = input("Are you a UK resident? ")

print("Hello " + first_name + " " + last_name)
print("Date of birth: " + DOB)
print("Course name is: " + course_name)
print("Answer to: Are you a UK resident: " + UK_resident)
 ```

```python
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
```

# How to set up Git and GitHub

## Install Git

1. Follow this link `https://git-scm.com/book/en/v2/Getting-Started-Installing-Git`
2. Follow the instructions on the website closely and ensure you are doing exactly what it tells you
    1. Here is a link for the git wizard `https://git-scm.com/download`

## What to do to make sure you run a program with administrator privileges every time

1. Find the executable for Git or your shortcut
2. Select it and go to `Properties/Compatibility`
3. Check the `Run this program as an administrator`
4. You're all set!

## Linking Git and GitHub

### Ensure you create the SSH key pair correctly using this link

`https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account`

1. Make an account for GitHub and make a new repository
2. The first page of the new repository will have instructions on how to link your git to github
3. Follow these as closely as you can as one skip or mess up will cause you a lot of problems

### Things that could go wrong

- You may not have access to something as you didn't start the program with admin privileges (refer to previous section
  to solve this)
- You did not do the SSH key pair correctly (ensure you follow the instructions here very closely)
- You pasted the private key on github instead of the public one (ensure the public key is pasted in that section)
- You did not initialise the folder you want to be a local repo as one (git init from git bash terminal)
- Your IDE or terminal keeps giving you `ssh: connect to host github.com port 22: Network is unreachable`
    - In this case specifically, you will need to create a config file to force SSH to use a specific port used for
      github
    - To do this open the `.ssh` folder in your bash terminal
    - Copy and paste the following commands in the terminal
        - `nano ~/.ssh/config`
        - Copy and paste this EXACTLY into the file you just opened
            - ```bash
      Host github.com
      Hostname ssh.github.com
      Port 443
        ```
        - To exit this editor
            - Press Ctrl + O (letter not number)
            - Press Enter
            - Press Ctrl + x
        - To see if you did it correctly use the following command
            - `ssh -T git@github.com`
            - If the command times out, you did something wrong, try it again
        - Next steps:
            - It will most likely as you a question with something called a "fingerprint"
            - Say "yes" to this, and agree to anything else
            - Run this command again `ssh -T git@github.com`
            - And it should say `Hi xxxx! You've successfully authenticated, but GitHub does no provide shell access`
            - That means you are done
            - You can now push from your PyCharm or any IDE

# Git and GitHub pushing

1. `git add .`
2. `git commit -m "message"`
3. `git push -u origin master`
4. `git status` to check status

<img src="../images/diagram2.png" title="git/github setup" alt="ez" width="600"/>

## Operators

### Mathematical

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division

### Comparison operators

- `>` more than?
- `<` less than?
- `==` is equal to?
- `!=` is NOT equal to?
- `>=` is greater than or equal to?
- `<=` is less than or equal to?

```python

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
```

# Boolean built-in methods

```python

greetings = "Hello World!"
print(greetings)
print(greetings.isalpha())  # checks if the string is comprised of alphabet values
print(greetings.islower())  # checks if the string only has lower case letters
print(greetings.startswith("H"))  # checks if the string greeting starts with a "H"
print(greetings.endswith("!"))  # checks if the string greeting ends with a special character
print(greetings.isdigit())  # checks if the variable is a digit

```

# String slicing

```python

# String indxing - starts from 0
# Hello World!
# 01234567891011
greetings = "Hello World!"

print(len(greetings))  # checks the length of object in brackets
print(greetings[:5])  # print the value of the variable up to the 5th element
print(greetings[-6:])  # print the value of the variable from the end to the 6th element going backwards

print(greetings[0:5])  # print the value of the variable from character 0 to character 5
print(greetings[6:12])  # print the value of the variable from character 6 to character 12
```

# String methods available

```python


# use var = string "nfrowbg              "
white_space = "lots of spaces at the end          "
print(len(white_space))

# strip() method removes white spaces at the end of the string
print(len(white_space.strip()))
print(len(white_space))

sample_text = "lots of text and lots more text"

print(sample_text.count("text"))

print(sample_text.lower())
print(sample_text.upper())
print(sample_text.capitalize())
print(sample_text[-6:].upper())
print(sample_text.replace("text", "code"))  # replaces the first argument with the second one in the variable


```

```python

# Task 2

first_name = input("Please enter your first name. ").capitalize()
last_name = input("Please enter your last name. ").capitalize()
DOB = input("Please enter your date of birth (dd/mm/yyyy). ")
house_num = int(input("Please enter your house number. "))
postcode = input("Please enter your postcode. ").upper()
course_name = input("Please enter your course name. ").lower().capitalize()

UK_resident = input("You are a UK resident. (True of False). ")
UK_resident = UK_resident.lower().capitalize()
UK_resident = bool(UK_resident)

# using Fstrings to simplify string manipulation 
print(f"Hello {first_name} {last_name}")
print(f"Date of birth: {DOB}")
print(f"Your address is: {house_num} {postcode}")
print(f"Course name is: {course_name}")
print(f"Answer to: Are you a UK resident: {UK_resident}")

```

# Data Collections

## Types

### Lists

```python

# declare by using: list = ["nvrfjei", "nfruiw", ""...]

# Apply DRY - don't repeat yourself
shopping_list = ["ketchup", "fanta", "eggs", "bread"]
# print(shopping_list)
# print(type(shopping_list))
# CRUD - Create Read Update Delete

# Add/Append item to list (add at end of list)
shopping_list.append("chicken")
# print(shopping_list)

# Replace item in list
shopping_list[2] = "ice cream"
# print(shopping_list)

# remove item from list at index 0
# print(shopping_list.pop(0))
# print(shopping_list)

# remove "fanta" from list
shopping_list.pop(1)
# print(shopping_list)
shopping_list.remove("bread")
# print(shopping_list)

# can lists have multiple data types?
multi_type = [1, 2, 3, "one", "two", "three"]
print(multi_type)
print(multi_type[2])
```

### Tuples

#### Immutable - cannot be changes - edited - added

```python
# user_details = DOB, country names, city names
# Syntax: ("hbte","are","","greagr"...)

essentials = ("milk", "paracetamol", "drinks")
print(essentials)
print(type(essentials))
# What is the difference between lists and tuples?
# essentials[0] = "coffee"
print(essentials)


```

### Dictionaries

```
```

<img src="../images/python_exercise_completion.png" title="Flex" alt="ez" width="600"/>
