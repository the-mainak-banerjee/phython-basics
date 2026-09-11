# Challenge: Raffle Drawing
# Build a feature that manages a charity raffle. The program picks a random winner but
# makes sure nobody wins twice. If the random winner has already won a prize, keep
# drawing a random winner until you land on someone new.
# 1. Draw a random name from entrants.
# 2. If that name is already in winners, keep drawing until you get one
#    that isn't.
# 3. Add the new winner to winners and print: "Winner: <name>"

entrants = ["Amara", "Diego", "Priya", "Leo", "Sofia", "Kwame"]
winners = ["Diego", "Sofia"]

import random

winner = random.choice(entrants)

while winner in winners:
    print(winner)
    winner = random.choice(entrants)

winners.append(winner)
print(f"Winner: {winner}")