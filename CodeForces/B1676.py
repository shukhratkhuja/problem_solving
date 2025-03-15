import sys

t = int(sys.stdin.readline().strip())
results = []

for _ in range(t):

    a = list(map(int, sys.stdin.readline().strip().split()))
    
    finalists = {a[0] if a[0] > a[1] else a[1], a[2] if a[2] > a[3] else a[3]}
    a.sort()

    if {a[2], a[3]} == finalists:
        results.append("YES")
    else:
        results.append("NO")

sys.stdout.write("\n".join(results) + "\n")
