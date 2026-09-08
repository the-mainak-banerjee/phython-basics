def serve_chai():
    chai_type = "Masala Chai"  # local scope
    print(f"Inside func {chai_type}")


chai_type = "Lemon"
serve_chai()
print(f"Outside func {chai_type}")


def chai_counter():
    chai_order = "Masala chai" #Enclosing Scope 

    def print_order():
        chai_order = "Ginger"
        print("Inner: ", chai_order)
    print_order()
    print("Outer: ", chai_order)

chai_order = "Lemon Tea"
chai_counter()
print("Global:", chai_order)
