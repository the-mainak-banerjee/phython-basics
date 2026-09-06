import csv

students = []
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is from {student["home"]}")


# We can use file.seek(0)  to go back to the beginning of the file.
