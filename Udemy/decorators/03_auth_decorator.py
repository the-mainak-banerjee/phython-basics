from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user):
        if user != "admin":
            print("Access denied: Admin only")
            return None #This is an optional line sometimes python wants explixit return from decorator functions
        else:
            return func(user)

    return wrapper


@require_admin
def acess_tea_inventory(user):
    print("Access granted to inventory")


acess_tea_inventory("admin")
acess_tea_inventory("user")