# Types
"""
Tuples
Lists
Dict
"""

# Lists
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

# Tuples
# Immutable - cannot be changes - edited - added
# user_details = DOB, country names, city names
# Syntax: ("hbte","are","","greagr"...)

essentials = ("milk", "paracetamol", "drinks")
print(essentials)
print(type(essentials))
# What is the difference between lists and tuples?
# essentials[0] = "coffee"
print(essentials)

