import sys

t = int(sys.stdin.readline().strip())

results = []
for _ in range(t):

    x, y = map(int, sys.stdin.readline().strip().split())

    if x > y:
        results.append(f"{y} {x}")
    else:
        results.append(f"{x} {y}")


sys.stdout.write("\n".join(results) + "\n")
