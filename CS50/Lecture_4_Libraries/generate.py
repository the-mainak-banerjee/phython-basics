# It will import everything from the random module
# import random

# It will only import the choice function from the random module
from random import choice, randint, shuffle

# Generate a random coin flip
coin = choice(['Heads', 'Tails'])
print(f'The coin landed on: {coin}')

# Generate a random integer between 1 and 10 (inclusive)
number = randint(1,10)
print(f'The random number is: {number}')

# Randomize a list of cards
cards =["Jack", "Queen", "King", "Ace"]
print(f'Original cards: {cards}')

shuffle(cards)
print(f'Shuffled cards: {cards}')