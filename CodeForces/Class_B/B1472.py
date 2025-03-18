import sys

t = int(sys.stdin.readline().strip())
results = []

for _ in range(t):

    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    ones = 0
    twos = 0

    for i in a:
        if i == 1:
            ones += 1
        else:
            twos += 1
    
    if (ones % 2 == 0 and twos % 2 == 0) or (twos % 2 == 1 and ones % 2 == 0 and ones != 0):
        results.append("YES")
    else:
        results.append("NO")

sys.stdout.write("\n".join(results) + "\n")
