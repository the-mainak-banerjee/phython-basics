def chai_flavour(flavour="masala"):
    # This is known as docstring, To know more about it check the type-hints.py file inside Lecture 9 of CS50
    """Return the flavour of the chai"""
    return flavour

# These __method__ methods are called dunder method.
print(chai_flavour.__doc__) #This will retun the doc string
print(chai_flavour.__name__) #This will return the name of the function