import csv

students = []

with open("students_home.csv") as file:
    reader = csv.reader(file)
    # We can also use name, home in place of row here
    for row in reader:
        print(row)
        students.append({"name": row[0], "home": row[1]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is from {student["home"]}")