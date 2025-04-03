"""
Gradient kvadrat
n x n maydonda markazdan uzoqlik bo‘yicha raqam yoki belgilar o‘sib boradi:

3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
"""
import math
n = int(input())
color = math.ceil(n / 2)

matrix = ""
for i in range(n):
    line = []
    for j in range(n):
        line.append(str(color - min(min(i, j), min(abs(n-i-1), abs(n-j-1)))).rjust(2))
    matrix += " ".join(line)
    matrix += "\n"

print(matrix)