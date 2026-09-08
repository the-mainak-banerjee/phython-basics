# pure functions
def chai_update(cups):
    return cups * 2


chai_sold = 200
# Impure function [Not recommended]
def chai_update_impure(cups):
    global chai_sold
    chai_sold += cups
    return chai_sold

# Recursive Func
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n - 1)

print(pour_chai(3))



# Lambda function: A lambda function in Python is a small anonymous function that takes arguments and returns the result of a single expression.
chai_types = ["light", "kadak", "ginger", "kadak"]
non_strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))
print(non_strong_chai)


# Is adult, using lambda function
is_adult = lambda age: "Adult" if age>=18 else "Child"
print(is_adult(20))


# Comprehensions as expresions of lambda functions
numbers = [2,4,6,8,10]
double_numbers = lambda x: [n*2 for n in x]
print(double_numbers(numbers))

# Just a side note we can achieve the above exmple by using map as well
triple_numbers = list(map(lambda number: number * 3, numbers))
print(triple_numbers)