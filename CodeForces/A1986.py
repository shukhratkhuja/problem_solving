import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    a = list(map(int,sys.stdin.readline().strip().split()))
    a.sort()

    answer = abs(a[1]-a[0]) + abs(a[1]-a[2])

    results.append(str(answer))


sys.stdout.write("\n".join(results) + "\n")
