import sys, math

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    a.sort()
    a[0] += 1
    results.append(str(math.prod(a)))

sys.stdout.write("\n".join(results) + "\n")
