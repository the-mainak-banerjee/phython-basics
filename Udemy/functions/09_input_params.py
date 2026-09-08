chai_type = "lemon"


def prepare_chai(chai):
    # This is immumatable and don't update the chai_type variable value
    print("Preparing: ", chai)

prepare_chai(chai_type)
print(chai_type)



chai = [1, 2, 3]
def edit_chai(cup):
    # This is mutable and update the original chai list
    cup[1] = 42

edit_chai(chai)
print(chai)




def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjelling", "Yes", "Low") #positional args
make_chai(tea="Green", sugar="Medium", milk="No") #keywords

def special_chai(*ingredients, **extras):
    # This will be tuple
    print("Ingredients", ingredients)
    # This will be dict
    print("Extras", extras)

special_chai("Cinnamon", "Cardamom", sweetner="Honey", foam="yes")


def chai_order(order =[]):
    order.append("masala")
    print(order)

chai_order()
chai_order()
# At the end of two calls we will actually get ["masala", "masala"] this is called default trap. To avoid this we can use the below code

# This happens because Python creates the default value only once, when the function is defined — not every time the function is called.


def chai_order_fixed(order=None):
    if order is None:
        order = []
    order.append("Masala")
    print(order)

chai_order_fixed()
chai_order_fixed()
# At the end of this we will only get ["Masala"] for both function call.

# Important rule: Avoid mutable objects ([], {}, set()) as default arguments. Use None and create the object inside the function instead.
