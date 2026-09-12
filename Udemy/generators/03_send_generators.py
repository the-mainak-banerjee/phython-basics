def chai_customer():
    print("Welcome! what chai you would you like?")
    order = yield
    while True:
        print(f"preparing {order}...")
        order = yield

stall = chai_customer()

next(stall)

stall.send("Lemon Tea")
stall.send("Ginger tea")