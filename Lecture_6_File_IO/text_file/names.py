# names = []

# for _ in range(3):
#     names.append(input("Name: "))

# # Sorted sort the list
# for name in sorted(names):
#     print(f"hello, {name}")

# Lets store the names in a file

name = input("Name: ");

# "a" stands for append here
file = open("names.txt", "a")
file.write(f"{name}\n");
file.close()

# We can automatically close the file after we are done with it by using the with statement.
with open("char_names.txt", "a") as file:
    file.write(f"{name}\n")

