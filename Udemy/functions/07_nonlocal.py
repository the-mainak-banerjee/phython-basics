def update_order():
    chai_type = "Elaichi"
    def kitchen():
        # This will access the variable from its parent
        nonlocal chai_type 
        chai_type = "Keshar"
    kitchen()
    print("After kitchen update:", chai_type)

update_order()