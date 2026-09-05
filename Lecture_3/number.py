def main():
    x = get_int("What's is x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("x is not an integer")
        else:
            return x


# Compact version of get_int function and this will catch the ValueError exception and do nothing, allowing the loop to continue until a valid integer is entered.

# def get_int():
#     while True:
#         try:
#             return int(input("What's is x? "))
#         except ValueError:
#             pass


main()

# Important notes:
# Here we can also use the isdigit() method to check if the input is a digit before converting it to an integer. This will prevent the ValueError exception from being raised in the first place. But the pythonic way is to use the try-except block as shown above.