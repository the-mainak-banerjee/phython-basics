def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")

    # This is a tupple and it is immutable, we can not do student[1] = "Ravenclaw", but list is mutable so in case of list we can do student[1] = "Ravenclaw"
    # return (name, house)

    # This is a list
    return [name, house]

# The best way to implement the get_student function is to use a dictionary, because we can use the key to access the value and we can also change the value of the key.

def get_student_dict():
    name = input("Name: ")
    house = input("House: ")

    # This is a dictionary
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
