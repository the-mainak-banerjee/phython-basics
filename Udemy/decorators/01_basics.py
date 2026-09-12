from functools import wraps


def my_decorator(func):
    # With out this @wraps the original function will loose its metadata like __name__ and all. __name__ will become wrapper instead of the function name (greetings as used in the code below) if we don't use @wraps
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")

    return wrapper


# This @my_decorator line make the greetings function runs as a decorator
@my_decorator
def greetings():
    print("Hello from Decorator")


greetings()
print(greetings.__name__)
