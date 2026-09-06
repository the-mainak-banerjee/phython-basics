# with open("students.csv") as file:
#     for line in file:
#         name, house =line.rstrip().split(",")
#         print(f"{name} is in {house}")


# Lets sort the data in the csv file
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_name(student):
    return student["name"]


# Here the get_name function is getting called by the sorted function for each student in the students list. The sorted function will use the return value of the get_name function to sort the students list.
for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")


print("--------------divider------------")


# We can also use a lambda function to sort the students list by name. A lambda function is an anonymous function that can take any number of arguments, but can only have one expression. The expression is evaluated and returned. The syntax for a lambda function is: lambda arguments: expression

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
