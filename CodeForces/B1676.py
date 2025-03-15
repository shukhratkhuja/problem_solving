import sys

t = int(sys.stdin.readline().strip())
results = []

for _ in range(t):

    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))

    min_candy = min(a)
    result = 0
    for i in a:
        if i != min_candy:
            result += i-min_candy
    
   
    results.append(str(result))

sys.stdout.write("\n".join(results) + "\n")
