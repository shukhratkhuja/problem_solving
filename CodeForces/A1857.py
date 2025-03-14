import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    if sum(a) % 2 == 0:
        results.append("YES")
    else:
        results.append("NO")

sys.stdout.write("\n".join(results) + "\n")
