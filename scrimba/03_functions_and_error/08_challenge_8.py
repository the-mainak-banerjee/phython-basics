# Challenge: Hot Dog Contest
# You're building a signup for a hot dog eating contest. Entrants type how many
# hot dogs they think they can eat, but nothing stops them from typing something
# that isn't a number.

# 1. Ask the entrant how many hot dogs they can eat and convert the answer to an int.
# 2. If the answer isn't a whole number, print "I need a number to sign you up."
# 3. If the answer is a whole number, print "Signed up for {count} hot dogs. Good luck!"

# Here's what your output should look like:
#
# How many hot dogs can you eat? 7
# Signed up for 7 hot dogs. Good luck!
#
# How many hot dogs can you eat? a lot
# I need a number to sign you up.

try:
    hot_dogs_count = int(input("How many hot dogs can you eat? "))
    print(f"Signed up for {hot_dogs_count} hot dogs. Good luck!")

except ValueError:
    print("I need a number to sign you up.")
