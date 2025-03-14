import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    h, m = map(int, sys.stdin.readline().strip().split())
    
    results.append(str((23 - h) * 60 + 60 - m))

sys.stdout.write("\n".join(results) + "\n")
