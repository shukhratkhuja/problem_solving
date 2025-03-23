import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    evens = 0
    for i in a:
        if i % 2 == 0:
            evens += 1

    # evens = sum(1 for i in a if a % 2 == 0)

    results.append("YES" if len(a) / 2 == evens else "NO")

sys.stdout.write("\n".join(results) + "\n")