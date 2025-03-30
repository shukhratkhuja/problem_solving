import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    s = sys.stdin.readline().strip()

    # print("ORIGINAL:", s)
    s = s[::-1]
    # print("REVERSED: ", s)
    s = s.replace('p', 'x').replace('q', 'p').replace('x', 'q')
    # print("REPLACED: ", s)
    results.append(s)


sys.stdout.write("\n".join(results) + "\n")
