# Read from a file
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())


# ------------------

print("--------------divider------------")

# ------------------

# Compact the above code using list comprehension, but these can't sort the values.
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

# ------------------

print("--------------topic change------------")

# ------------------

# Lets sort the data now

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

# ------------------

print("--------------divider------------")

# ------------------

# We can compact the above code as well
with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print("hello,", line.rstrip())
