import sys

t = int(sys.stdin.readline().strip())
results = []

for _ in range(t):

    n, k = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))

    results.append("YES" if k in a else "NO")

sys.stdout.write("\n".join(results) + "\n")
