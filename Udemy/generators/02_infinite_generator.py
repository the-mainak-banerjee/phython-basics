def infinite_chai():
    count = 1
    while True:
        yield "Chai"
        count+= 1

customer_1 = infinite_chai()
customer_2 = infinite_chai()

for _ in range(3):
    print(next(customer_1))

print("_" * 40)
for _ in range(4):
    print(next(customer_2))
