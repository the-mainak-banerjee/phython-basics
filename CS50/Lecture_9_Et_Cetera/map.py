def main():
    yell("This", "is", "CS50")

def yell(*words):
    # map() is a built-in function used to apply the same function to every item in an iterable (like a list, tuple, etc.).
    uppercase = map(str.upper, words)
    print(*uppercase)

    # This technique is known as list comprehensions
    uppercase_list = [word.upper() for word in words]
    print(*uppercase_list)

if __name__ == "__main__":
    main()
