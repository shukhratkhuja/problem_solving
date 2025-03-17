import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()

    counter = 0
    while s[0] != s[-1]:
        s = s[1:-1]
        counter += 1
        if s == '':
            break
    results.append(str(n-counter*2))


sys.stdout.write("\n".join(results) + "\n")
