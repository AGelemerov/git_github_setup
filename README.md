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
- You may not have access to something as you didn't start the program with admin privileges (refer to previous section to solve this)
- You did not do the SSH key pair correctly (ensure you follow the instructions here very closely)
- You pasted the private key on github instead of the public one (ensure the public key is pasted in that section)
- You did not initialise the folder you want to be a local repo as one (git init from git bash terminal)
- Your IDE or terminal keeps giving you `ssh: connect to host github.com port 22: Network is unreachable`
  - In this case specifically, you will need to create a config file to force SSH to use a specific port used for github
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

# Python Intro
## Data types
## Operators
### Mathematical
- `+`
- `-`
- `*`
- `/`

### Comparison operators
- `>`
- `<`
- `==`
- `!=`
- `>=`
- `<=`
