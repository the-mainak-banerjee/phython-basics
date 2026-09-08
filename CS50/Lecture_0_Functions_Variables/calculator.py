# We can also use int as well as float to get the input from the user. The difference is that int will only accept whole numbers while float will accept decimal numbers as well.
x = float(input("What is x? ")) 
y = float(input("What is y? "))

# round will round the number to the nearest integer. If you want to round to a specific number of decimal places, you can use the second argument of the round function. For example, round(x, 2) will round x to 2 decimal places.
# sum = round(x + y)
div = round(x / y, 2)



print(div)

# print(f"{sum:,}.") => It will render like 1,000,000 instead of 1000000. It is a good way to format numbers with commas for better readability.

# print(f"{div:.2f}.") => It will render like 1.23 instead of 1.23456789. It is a good way to format numbers to a specific number of decimal places for better readability.