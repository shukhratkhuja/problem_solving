import sys, math

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    results.append(str(math.ceil(n/2)))


sys.stdout.write("\n".join(results) + "\n")
