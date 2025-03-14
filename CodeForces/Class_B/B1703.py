import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()

    sl = [c for c in s]
    results.append(str(len(sl) + len(set(sl))))
sys.stdout.write("\n".join(results) + "\n")
