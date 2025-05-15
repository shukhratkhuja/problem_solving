import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    a,b,c,d = map(int, sys.stdin.readline().strip().split())
    if b + b > c:
        results.append(f"{b} {b} {c}")
    else:
        results.append(f"{b} {c} {c}")


sys.stdout.write("\n".join(results) + "\n")
