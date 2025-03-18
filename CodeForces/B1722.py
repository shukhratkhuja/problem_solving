import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    a = a.replace('G', 'B')
    b = b.replace('G', 'B')

    results.append("YES" if a == b else "NO")


sys.stdout.write("\n".join(results) + "\n")
