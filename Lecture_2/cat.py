i = 0

while i < 3:
    print("Meow")
    i += 1

# Using for loop
for i in [0, 1, 2]:
    print("Meow meow")

for i in range(3):
    print("Meow meow mewo")

# Since we are not using i in our program we can do this:

for _ in range(3):
    print("Meow meow mewo")

# Without loop
print("Meow Print\n" * 3, end="")

# Take input from user and print "Meow" that many times
while True:
    n = int(input("What's is n? "))
    if n > 0:
        break

for _ in range(n):
    print("Meow")

# USe function


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's is the value n? "))
        if n > 0:
            break
    return n


def meow(number):
    for _ in range(number):
        print("Meow")


main()
