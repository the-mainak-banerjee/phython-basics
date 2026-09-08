import sys
import argparse

def main():
    # use_sys()
    use_arg()

# Using sys
def use_sys():
    if len(sys.argv) == 1:
        print("Meow")
    elif len(sys.argv) == 3 and sys.argv[1] == "-n":
        n = int(sys.argv[2])
        for _ in range(n):
            print("Meow")
    else:
        print("usage: argparse.py")

# Using Argparse
def use_arg():
    parser = argparse.ArgumentParser(description="Meow like a cat")
    parser.add_argument("-n", default=1, help="number of times to meow", type=int)
    args = parser.parse_args()
    for _ in range(args.n):
        print("Meow")


if __name__ == "__main__":
    main()