import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    a.sort()

    differences = [a[i]-a[i-1] for i in range(1, n)]

    results.append(str(min(differences)))
    
sys.stdout.write("\n".join(results) + "\n")
