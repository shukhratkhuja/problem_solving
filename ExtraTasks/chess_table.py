import sys

t = int(sys.stdin.readline().strip())
results = []

for _ in range(t):

    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = ""
        for j in range(n):
            if i % 2 == j % 2:
                line += ".."
            else:
                line += "##"
        results.append(line)
        results.append(line)

sys.stdout.write("\n".join(results) + "\n")
