# Dictionary basics :D

# 1 - Define a dictionary call story1, it should have the following keys:
# 'start', 'middle' and 'end'

# 2 - Print the entire dictionary

# 3 - Print the type of your dictionary

# 4 - Print only the keys

# 5 - print only the values

# 6 - print the individual values using the keys (individually, lots of print commands)

# 7 - Now let's add a new key:value pair.
# 'hero': yourSuperHero

"""
-------------SOLUTION-------------
"""
# 1
story1 = {
    "start": ["Her job was being paid to follow an elderly widow around her own house.",
              "The client had a depressed waxy smile, one that seemed stuck on her face since she lost her husband in "
              "the flood."],

    "middle": ["There were the heavy sighs of the toilet and they floated around her ears. ",
               "She would stand there, just outside the door while the woman allowed all of her sadness to dribble "
               "out. "],
    "end": ["The sound was like something you'd find in nature.",
            "\"Shhh,\" the old woman would say, \"I'm letting go of him again.\""]
}

# 2
print(story1)

# 3
print(type(story1))

# 4
print(story1.keys())

# 5
print(story1.values())
print()  # just to separate

# 6
print(story1["start"][0])
print(story1["start"][1])
print(story1["middle"][0])
print(story1["middle"][1])
print(story1["end"][0])
print(story1["end"][1])

# 7
new_dict_elems = {
    "hero": "Dr.Strange"
}
story1.update(new_dict_elems)
print()
print(story1)
print(story1["hero"])
