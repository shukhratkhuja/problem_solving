import sys

t = int(sys.stdin.readline().strip())
results = []

for _ in range(t):

    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    max_zero = 0
    current_zero = 0
    
    for i in a:
        if i == 0:
            current_zero += 1
        else:
            max_zero = max(max_zero, current_zero)
            current_zero = 0

    results.append(str(max(max_zero, current_zero)))

sys.stdout.write("\n".join(results) + "\n")
