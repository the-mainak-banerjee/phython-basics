# Without using Pytest
# from calculator import square

# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")

#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")

#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")

#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared was not 9")


# if __name__ == "__main__":
#     main()

# With Using Pytest

import pytest
from calculator import square

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0

# We can also divide the test cases into separate functions for better organization and readability.

def test_square_positive_numbers():
    assert square(2) == 4
    assert square(3) == 9

def test_square_negative_numbers():
    assert square(-2) == 4
    assert square(-3) == 9  

def test_square_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("Cat")