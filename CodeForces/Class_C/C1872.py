import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):
    
    a = []
    points = 0
    
    for _ in range(10):
        l = sys.stdin.readline().strip()
        a.append(l)
    
    for i in range(10):
        for j in range(10):
            if a[i][j] == 'X':
                d = min(i, j, 9 - i, 9 - j)
                points += d + 1

    results.append(str(points))


sys.stdout.write("\n".join(results) + "\n")
