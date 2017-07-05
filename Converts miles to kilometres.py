def km(miles = 0):
    """Converts a length from miles to kilometres)"""
    miles_to_km = miles * 1.609344
    return miles_to_km

m = input()

try:
    m = float(m)
    print (km(miles = m))
except ValueError:
    print("That's not a number!")
