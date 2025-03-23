import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    results.append(str(n-1))

sys.stdout.write("\n".join(results) + "\n")
