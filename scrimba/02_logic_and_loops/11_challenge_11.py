# Challenge: Boarding Passes
# You're building an airport app that prints a boarding pass for each
# passenger on a group booking.
# Write a while loop that prints one line per passenger, like this:
# "Printing boarding pass 1 of 5..."
# "Printing boarding pass 2 of 5..."
# ...and so on until the last passenger.

PASSENGERS = 5
passenger_num = 1

while passenger_num <= PASSENGERS:
    print(f"Printing boarding pass {passenger_num} of {PASSENGERS}...")
    passenger_num += 1