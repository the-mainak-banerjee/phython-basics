def main():
    total_by_dict()
    f(100, 25, 50, galleons=100, sickles = 25, knuts = 50)

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


def total_by_list():
    coins = [100,50,25]
    # This syntax is unpacking the list
    print(total(*coins), "Knuts")

def total_by_dict():
    coins = {"galleons": 100, "sickles": 50, "knuts": 25}
    # This syntax is unpacking the dic
    print(total(**coins), "Knuts")

def f(*args, **kwargs):
    # *args means the function can take  variable number of arguments
    print("Positional args, which is a Tuple", args)
    # *kwargs means the function can take variable number of named arguments
    print("Named args, which is a dict", kwargs)

if __name__ == "__main__":
    main()
