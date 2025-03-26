import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    a = list(map(int, sys.stdin.readline().strip().split()))

    for _ in range(5):
        a.sort()
        a[0] += 1

    results.append(str(a[0] * a[1] * a[2]))

sys.stdout.write("\n".join(results) + "\n")
