import sys

t = int(sys.stdin.readline().strip())

results = []

for _ in range(t):
    w, h, n = (map(int, sys.stdin.readline().strip().split()))

    answer = 1
   
    while answer < n:
        
        if w % 2 == 0:
            answer *= 2
            w //= 2
        elif h % 2 == 0:
            answer *= 2
            h //= 2
        else:
            results.append("NO")
            break
    else:
        results.append("YES")
    
sys.stdout.write("\n".join(results) + "\n")
