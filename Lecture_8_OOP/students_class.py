# This is withot constructor, we can use the constructor to initialize the instance variables.

# class Student:
#    ...


class Student:
    def __init__(self, name, house):
        # We are not using _house or _name here because we want this assignment will also go through the setter function and with propoer validation check inside it
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is in {self.house}"

# Instance Methods: Writing function inside of classes that are automatically passed a reference to self, the current object.

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, name):
        if not name:
            # Use this in your own to raise any error
            raise ValueError("Missing Name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Shytherin"]:
            raise ValueError("Invalid House")
        self._house = house


def main():
    student = get_student()
    # Even after creating all those getter and setter functions we can still do the below line and change the value of any variable to an invalid value. So as a developer we need to remeber to not touch a variable start with _ or __.
    # student._house = "India"
    print(student)



# Use constructor to initialize the instance variables.
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
