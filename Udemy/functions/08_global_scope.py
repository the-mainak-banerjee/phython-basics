chai_type = "Plain"

def front_desk():
    def kitchen():
        # This will access the variable defined in global scope.
        global chai_type
        chai_type = "Irani"
    kitchen()

front_desk()
print("Final Global chai:", chai_type)
