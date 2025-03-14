import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    s = sys.stdin.readline().strip()
    results.append("A" if s.count("A") > s.count("B") else "B")

sys.stdout.write("\n".join(results) + "\n")
