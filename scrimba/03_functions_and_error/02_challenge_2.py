# Challenge: Write two functions with parameters
# Write each function underneath its instructions, then call it with the values given.

# 1. Write a function called add_numbers that prints the sum of the two numbers you pass in.
#    Call it a couple of times with different numbers.
#    Example output:
#    add_numbers(2, 3) prints 5
#    add_numbers(10, 45) prints 55


# 2. You've scrambled a word before: turn it into a list of letters, shuffle them, and
#    join them back together. Let's make that reusable. Write scramble(word) so it takes
#    any word and prints a scrambled version of it.
#    Example output:
#    scramble("python") might print nohtyp

import random

def add_number(num_1, num_2):
    sum = num_1 + num_2
    print(sum)

add_number(2,3)
add_number(10,45)

def scramble(word):
    char_list = list(word)
    random.shuffle(char_list)
    scrambled_word= "".join(char_list)
    print(scrambled_word)

scramble("python")