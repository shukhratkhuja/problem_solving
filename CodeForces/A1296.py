import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    answer = "NO"

    if sum(a) % 2 == 1:
        answer = "YES"
    else:
        has_evens, has_odds = False, False
        for i in a:
            if i % 2 == 0:
                has_evens = True
            else:
                has_odds = True
            
            if has_evens and has_odds:
                answer = "YES"
                break
    
    results.append(answer)

sys.stdout.write("\n".join(results) + "\n")
