import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    s = sys.stdin.readline().strip()

    results.append(s[:-2]+'i')


sys.stdout.write("\n".join(results) + "\n")
