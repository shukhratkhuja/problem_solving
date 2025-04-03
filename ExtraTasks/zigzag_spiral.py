"""
Zigzag spiral
Matritsani zigzag tarzda to‘ldir (1, 2, 3... bilan):

1  2  3  4
8  7  6  5
9 10 11 12
16 15 14 13

"""

n = int(input())

counter = 1
matrix = ""
for i in range(n):
    line = ""
    
    for j in range(n):
        line += f"{counter:>3}"

        if i % 2 == 0:
            counter += 1
        else:
            counter -= 1
    matrix += line
    matrix += "\n"

    if i % 2 == 0:
        counter += n-1
    else:
        counter += n+1

print(matrix)