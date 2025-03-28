import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    a, b = map(int,sys.stdin.readline().strip().split())
    
    if a > b: results.append("1" if (a - b) % 2 == 0 else "2")
    elif a < b: results.append("1" if (b - a) % 2 == 1 else "2")
    else:
        results.append('0')


sys.stdout.write("\n".join(results) + "\n")
