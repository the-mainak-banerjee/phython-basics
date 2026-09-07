from random import choice

class Hat:
    # This is class variable and we can only have one copy of this
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Shytherin"]

    # This is called class method
    @classmethod
    def sort(cls, name):
        house = choice(cls.houses)
        print(name, "is in", house)

# Note: In case of using class method we no need to do this:
# hat = Hat()


Hat.sort("harry")
