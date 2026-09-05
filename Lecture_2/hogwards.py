# List in python
students = ["Harry", "Ron", "Harmione"]

for student in students:
    print(student)


print(len(students))

for i in range(len(students)):
    print(i + 1, students[i])


# Dictionary in python
students_dict = {
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Harmione": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students_dict:
    print(student, students_dict[student], sep=", ")


# List of dictionaries
students_list = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Harmione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students_list:
    print(student["name"], student["house"], student["patronus"], sep=", ")