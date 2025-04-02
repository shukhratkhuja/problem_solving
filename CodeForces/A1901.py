import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n, x = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    max_dif = max([a[i] - a[i-1] for i in range(1, n)]+[a[0]]) if n > 1 else a[0]
    
    if  max_dif > (x - a[-1]) * 2:
        results.append(str(max_dif))
    else:
        results.append(str((x - a[-1]) * 2))

sys.stdout.write("\n".join(results) + "\n")
