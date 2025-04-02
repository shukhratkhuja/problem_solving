import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n, k = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))


    if k == 1:
        if a == sorted(a):
            results.append("YES")
        else:
            results.append("NO")
    else:
        results.append("YES")


sys.stdout.write("\n".join(results) + "\n")
