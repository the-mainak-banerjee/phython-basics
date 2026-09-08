import sys

# The first argument is the name of the script itself, so we can ignore it
print(sys.argv)

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print(f"Hello my name is {sys.argv[1]}")


# Another updated version of the same by using the exit function of sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print(f"Hello my name is {sys.argv[1]}")

# Slice in Python for lists

for args in sys.argv[1:]:
    print(args)
