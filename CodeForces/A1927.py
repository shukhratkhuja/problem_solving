import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    
    results.append(str(s.rindex('B')-s.index('B')+1))

sys.stdout.write("\n".join(results) + "\n")
