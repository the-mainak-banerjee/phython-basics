# Challenge: Call the Next Guest
# call_next() seats the first guest on a restaurant's waitlist. But when the waitlist is empty, the app crashes.

waitlist = []


def call_next(waitlist):
    """Seat the first guest on the waitlist."""
    if len(waitlist) == 0:
        print("The waitlist is empty")
        return
    name = waitlist[0]
    print(f"Now seating: {name}")


# 1. Add a guard clause to call_next() that exits early when the waitlist is empty,
#    and prints a message instead of crashing.
# 2. Test it with an empty waitlist to confirm it no longer crashes.
call_next([])