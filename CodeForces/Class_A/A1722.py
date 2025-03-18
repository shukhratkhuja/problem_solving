import sys

t = int(sys.stdin.readline().strip())

results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    if n != 5: results.append("NO")
    else:
        if set(c for c in s) == {'T', 'i', 'm', 'u', 'r'}:
            results.append("YES")
        else: results.append("NO")
    
sys.stdout.write("\n".join(results) + "\n")
    
