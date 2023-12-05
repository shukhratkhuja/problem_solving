from math import asin, pi, atan, degrees

c = int(input())
a = int(input())
phi = round(atan(c/a) / pi * 180)
print(f"{phi}{chr(176)}")

# r = abs(complex(c, a))
# phi = degrees(asin(c/r))
# print(round(phi))
