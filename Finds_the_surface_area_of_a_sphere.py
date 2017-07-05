import math

def area(r):
    """Returns the area of a sphere with radius r"""
    a = 4 * math.pi * r**2
    return a

r = input()

try:        #This will convert the input of r into a float to see if it can be computed, if it cannot i.e. it is not a number, then the program ends
    r = float(r)
    print (area(r))
except ValueError:
    print("That's not a number!")
