import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):
    x, y = 0, 0
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()

    answer = "NO"
    for c in s:
        if c == 'R': x += 1
        elif c == 'L': x -= 1
        elif c == 'U': y += 1
        elif c == 'D': y -= 1

        if x == 1 and y == 1:
            answer = "YES"
            break
    
    results.append(answer)


sys.stdout.write("\n".join(results) + "\n")
