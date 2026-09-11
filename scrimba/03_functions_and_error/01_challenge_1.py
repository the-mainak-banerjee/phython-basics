# Challenge: Write some functions!
# You've very generously decided to pick up coffee for six of your favorite coworkers this morning.

# 1. Write a function announcing your coffee run.
# Example output: "I am headed to the coffee shop! Who wants a latte?"

# 2. Write a function to calculate the total cost if you buy them each a latte for $5. In an f string, print how many lattes and what the total comes to.
# Example output:
# 6 lattes comes to $30.

# 3. Your coworkers thank you profusely. To save a little time, write a function that prints "You're welcome!" twice, then call it as many times as you need to thank all six coworkers.

# 4. Put all your function calls in a new function called coffee_run(), and call it to start your coffee run!


def announce_coffe_run():
    print("I am headed to the coffee shop! Who wants a latte?")


def calculate_price():
    total = 6
    coffe_price = 5
    total_price = total * coffe_price
    print(f"{total} lattes comes to ${total_price}")

def thanks():
    print("You are wellcome")
    print("You are wellcome")


def coffe_run():
    announce_coffe_run()
    calculate_price()
    thanks()
    thanks()
    thanks()

coffe_run()