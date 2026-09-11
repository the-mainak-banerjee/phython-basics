# Challenge: Build a Support Queue
# You're building a help desk feature that shows who's waiting
# in line for support.

# Use indexing to print a status display that looks like this:
#
#   Now helping: Ada
#   Next in line: Grace
#   Just added: Alan
#
# "Now helping" is the first person in line, "Next in line" is second, and "Just added" is the last person in the queue.

tickets = ["Ada", "Grace", "Linus", "Margaret", "Alan"]

now_helping = tickets[0]
next_in_line = tickets[1]
just_added = tickets[-1]

print(f"Now helping: {now_helping}")
print(f"Next in line: {next_in_line}")
print(f"Just added: {just_added}")
