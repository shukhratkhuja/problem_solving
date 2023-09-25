n = int(input())
sides = 0
shapes = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

for _ in range(n):
    shape = input()
    sides += shapes[shape]
    # if shape == "Tetrahedron":
    #     sides += 4
    # elif shape == "Cube":
    #     sides += 6
    # elif shape == "Octahedron":
    #     sides += 8
    # elif shape == "Dodecahedron":
    #     sides += 12
    # elif shape == "Icosahedron":
    #     sides += 20
    # else:
    #     print("ERROR")
print(sides)
