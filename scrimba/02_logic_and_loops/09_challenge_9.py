# Challenge: Data Cleanup
# You're building a sign-up form that tidies up whatever users type in.
# Each value below comes in messy. Figure out which string method (or
# methods) gets it to the clean version, then print the result. Some need
# just one method, and some need two chained together:
# 1. promo_code    "spring25"             ->  "SPRING25"
# 2. full_name     "jamie rivera"         ->  "Jamie Rivera"
# 3. email         "  Jamie@Example.COM"  ->  "jamie@example.com"
# 4. display_name  "  the ROCK  "         ->  "The Rock"

promo_code = "spring25"
full_name = "jamie rivera"
email = "  Jamie@Example.COM"
display_name = "  the ROCK  "

print(promo_code.upper())
print(full_name.title())
print(email.strip().lower())
print(display_name.strip().title())
