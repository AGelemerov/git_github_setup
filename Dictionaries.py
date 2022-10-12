"""  File to discuss dicts
Another Data Collection type
What is a dictionary
How to manage data using dicts

Works as a key-value pair
Syntax - { "key" : "value" }
not necessarily "" for strings
"""

# { "name" : "Sparta" }

# store student data - name, course_name, progress, completed_lessons
student_1 = {
    "name": "Angel",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["lists", "tuples", "OOP"]
}

# print(type(student_1))
# print(student_1["stream"])  # prints value saved in "stream"
# print(student_1["completed_lessons_names"])
# print(student_1["completed_lessons_names"][0])

# direct update of element
student_1["completed_lessons"] = 3
# print(student_1["completed_lessons"])

# delete and item from list
# print(student_1["completed_lessons_names"])

# student_1["completed_lessons_names"].remove("OOP")
# print("Removed OOP")

# print(student_1["completed_lessons_names"])

# print only keys
print(student_1.keys())

# print only values
print(student_1.values())
