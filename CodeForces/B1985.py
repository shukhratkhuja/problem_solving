import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    
    results.append('2' if n > 3 or n == 2 else '3')


sys.stdout.write("\n".join(results) + "\n")
