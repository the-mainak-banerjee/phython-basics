def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to = "world"):
    # """Print a greeting to the user. But this will not able to handle test cases properly."""
    # print(f"hello, {to}")

    # """So we can use the return statement to return the greeting instead of printing it. This will allow us to test the function properly."""
    return f"hello, {to}"


if __name__ == "__main__":
    main()