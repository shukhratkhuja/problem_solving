import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n, m = map(int, sys.stdin.readline().strip().split())
    s = sys.stdin.readline().strip()
    
    answer = 0
    
    for i in 'ABCDEFG':

        if m > s.count(i):
            answer += m - s.count(i)
    
    results.append(str(answer))

sys.stdout.write("\n".join(results) + "\n")
