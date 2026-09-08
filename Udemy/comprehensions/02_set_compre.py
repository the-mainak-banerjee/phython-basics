my_chai_orders = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai",
]


unique_chai_order = {chai for chai in my_chai_orders}

print(unique_chai_order)

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black peeper", "clove"],
}


unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
