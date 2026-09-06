# Please install this cowsay package by using pip install cowsay
import cowsay
import sys

if len(sys.argv) == 2:
    # cowsay.cow("hello ," + sys.argv[1])
    cowsay.pig("hello ," + sys.argv[1])
