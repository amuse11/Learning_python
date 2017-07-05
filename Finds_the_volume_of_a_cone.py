import math

def volume_cone(r, h):
    v = math.pi * r**2 * h/3
    return v

print ("Please input the radius and height of the cone.")
r = input()
h = input()

try:
    r = float(r)
    h = float(h)
    print (volume_cone(r, h))
except ValueError:
    print("That's not a number!")
