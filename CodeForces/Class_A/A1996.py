import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    results.append(str(n//4+1) if n%4==2 else str(n//4) )


sys.stdout.write("\n".join(results) + "\n")
