# Number of Polygons:
t = int(input())

for i in range(t):
    # Number of sides of the Polygon:
    n = int(input())
    if n % 4 == 0 and n > 2:
        print("YES")
    else:
        print("NO")
