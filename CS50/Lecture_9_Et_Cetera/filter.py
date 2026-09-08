students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# This is list_comprehensions
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)


print("\n--------------------\n")

# This is the filter version
def is_gryffindor(student):
    return student["house"] == "Gryffindor"

# gryffindors_filter = filter(is_gryffindor, students)
gryffindors_filter = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors_filter, key=lambda student: student["name"]):
    print(gryffindor["name"])
