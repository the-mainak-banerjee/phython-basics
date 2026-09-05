def main():
    name = input("What is your name? ")
    hello(name)

    x = int(input("What is x? "))
    print(f"{x} squared is {square(x)}")

    

# We are passing a default value to the hello function. If the user does not provide a name, it will default to "world".
def hello(to="world"):
    print(f"Hello, {to.strip().title()}!")

def square(x):
    # There are multiple ways to calculate the square of a number in Python. You can use the ** operator, the pow() function, or simply multiply the number by itself. Here are some examples:
    # return x * x
    # return x ** 2
    return pow(x, 2)

main()