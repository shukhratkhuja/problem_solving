import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    b = sorted(a)
    max_score = b[-1]
    sec_max_score = b[-2]

    d = [i - max_score if i != max_score else max_score-sec_max_score for i in a]
    
    results.append(" ".join(map(str, d)))


sys.stdout.write("\n".join(results) + "\n")
