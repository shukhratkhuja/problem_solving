import sys

t = int(sys.stdin.readline().strip())
results = []

for _ in range(t):

    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    results.append("YES" if len(a) == len(set(a)) else "NO")

sys.stdout.write("\n".join(results) + "\n")
