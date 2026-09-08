
# Version 1
# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")

# number:int = int(input("Number: "))
# # This will through an error in this version of code
# meows = meow(number)
# print(meows)

# Version 2
def meow_v2(n:int) -> str:
    """
    Meow n times

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

number:int = int(input("Number: "))
meows:str = meow_v2(number)
print(meows, end="")


# The below block is called DocString
#    """
#     Meow n times

#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A string of n meows, one per line
#     :rtype: str
#     """