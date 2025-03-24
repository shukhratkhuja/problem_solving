import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    
    max_q = 0
    x = -1
    max_words = 0
    for i in range(n):
        a, b = map(int, sys.stdin.readline().strip().split())
        if b > max_q and a <= 10:
            x = i
            max_q = b
        
    results.append(str(x+1))


sys.stdout.write("\n".join(results) + "\n")