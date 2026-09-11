# Challenge: Discount Code
# You're building a promo code checker for an online shop, so a shopper
# can enter a code and find out whether it unlocks the flash sale discount.

# 1. Prompt the user to enter a promo code. Hint: use an input() prompt.
# 2. Print whether the user's input is equal to promo_code.
# 3. Print whether the user's input is NOT equal to promo_code.
# 4. Enter both "FLASH50" and "flash50" as a prompt. Notice that because == is case-sensitive, the results will flip.

promo_code = "FLASH50"

user_promo_code = input("Enter your promo code: ")
print(promo_code == user_promo_code)
print(promo_code != user_promo_code)