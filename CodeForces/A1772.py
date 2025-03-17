import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    s = sys.stdin.readline().strip()
    results.append(str(eval(s)))

sys.stdout.write("\n".join(results) + "\n")
