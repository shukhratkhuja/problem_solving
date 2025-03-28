import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    answer = sum(i if i%2==0 else -i for i in a)
    results.append("YES" if answer > 0 else "NO")

sys.stdout.write("\n".join(results) + "\n")
