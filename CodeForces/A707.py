import sys

n, m = map(int, sys.stdin.readline().strip().split())
colors = []
result = "#Black&White"

for _ in range(n):
    a = list(sys.stdin.readline().strip().split())
    colors.append(a)
    if 'C' in a or 'M' in a or 'Y' in a:
        result = "#Color"
    

sys.stdout.write("\n"+ result + "\n")
