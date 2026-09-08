balance = 0

def main():
    print("balance: ", balance)
    deposit(100)
    print("balance: ", balance)
    withdraw(50)
    print("balance: ", balance)


def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount

# The same problem can be solved by using OOP. Please check the file bank.py in the folder Lecture_9


if __name__ == "__main__":
    main()