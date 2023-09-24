n = int(input())
sides = 0
for _ in range(n):
    shape = input()
    if shape == "Tetrahedron":
        sides += 4
    elif shape == "Cube":
        sides += 6
    elif shape == "Octahedron":
        sides += 8
    elif shape == "Dodecahedron":
        sides += 12
    elif shape == "Icosahedron":
        sides += 20
    else:
        print("ERROR")
print(sides)
