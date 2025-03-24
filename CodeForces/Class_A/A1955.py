import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n, a, b = map(int, sys.stdin.readline().strip().split())
    
    if 2 * a <= b:
        results.append(str(n*a))
    else:
        results.append(str(n//2*b+n%2*a))

sys.stdout.write("\n".join(results) + "\n")
