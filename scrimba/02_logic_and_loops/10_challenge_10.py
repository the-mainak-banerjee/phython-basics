# Challenge: Inventory Check
# Build an inventory display feature for a small office supply store.
# 1. Unpack the item and quantity for each entry in the list of tuples.
# 2. Print each item and it's quantity in this format: "notebooks: 42 in stock"

inventory = [
    ("notebooks", 42),
    ("pens", 130),
    ("staplers", 8),
]


item, quantity = inventory[0]
print(f"{item}: {quantity} in stocks")

item,quantity = inventory[1]
print(f"{item}: {quantity} in stocks")

item, quantity = inventory[2]
print(f"{item}: {quantity} in stocks")
