import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = sys.stdin.readline().strip()
    if len(n) < 3:
        print("NO")
    elif n[:2] == '10' and int(n[2:]) > 1 and n[2] != '0':
        print("YES")
    else:
        print("NO")
