import math

def volume_cone(r, h):
    v = math.pi * r**2 * h/3
    return v

print ("Please input the radius and height of the cone, and the units")
r = input()
h = input()
units = input()

try:
    r = float(r)
    h = float(h)
    print((volume_cone(r, h)), str(units))
except ValueError:
    print("The radius and/or height is not a number!")
