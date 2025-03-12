import sys

t = int(sys.stdin.readline().strip())

results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    if (n - 1) % 3 == 0 or (n + 1) % 3 == 0:
        results.append("First")
    else:
        results.append("Second")

sys.stdout.write("\n".join(results) + "\n")
    

