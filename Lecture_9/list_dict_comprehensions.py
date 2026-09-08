students = ['Hermione', "Harry", "Ron"]

# list comprehension to create another list
students_upper = [student.upper() for student in students]
print(students_upper)

print("\n--------------------\n")

# list comprehension to create another list of dict
gryffindors = [{"name": student, "house": "Gryffindors"} for student in students]
print(gryffindors)

print("\n--------------------\n")

# dict comprehension to create another dict
houses = {student: "Gryffindors" for student in students}
print(houses)