# This is a constant variable. It should not be changed.
MEOW = 3

for _ in range(MEOW):
    print("Meow")


class Cat:
    # This is a class constant
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("Meow")


cat = Cat()

cat.meow()