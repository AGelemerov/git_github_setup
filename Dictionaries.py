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
    "completed_lessons_names": ["lists", "tuples", "strings"]
}

print(type(student_1))
print(student_1["stream"])  # prints value saved in "stream"
print(student_1["completed_lessons_names"])
print(student_1["completed_lessons_names"][0])
