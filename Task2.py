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

print(f"Hello {first_name} {last_name}")
print(f"Date of birth: {DOB}")
print(f"Your address is: {house_num} {postcode}")
print(f"Course name is: {course_name}")
print(f"Answer to: Are you a UK resident: {UK_resident}")
