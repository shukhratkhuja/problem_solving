import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):
    
    a = []
    n = int(sys.stdin.readline().strip())
    
    for _ in range(n):
        a.append(sys.stdin.readline().strip())
    
    result = []
    for l in a[::-1]:
        result.append(str(l.index('#')+1))

    results.append(' '.join(result))

sys.stdout.write("\n".join(results) + "\n")
