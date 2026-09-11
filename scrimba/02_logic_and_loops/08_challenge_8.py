# Challenge: Wi-Fi Signal
# You're building a feature for a coffee shop that has spotty wi-fi. The feature should give
# customers a discount based on how many signal bars they're getting.
# Write an if/elif/else chain that prints a message for the customer's discount:
#   0 bars: "50% off, sorry about the Wi-Fi!"
#   1 or 2 bars: "25% off"
#   3 or 4 bars: "10% off"
#   5 bars: "Full bars, no discount today!"

signal = 4 # out of 5 bars

if signal == 5:
    print("Full bars, no discount today!")
elif signal>=3:
    print("10% off")
elif signal >= 1:
    print("25% off")
else:
    print("50% off, sorry about the Wi-Fi!")
