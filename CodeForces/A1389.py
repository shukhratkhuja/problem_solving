import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):

    l, r = map(int, sys.stdin.readline().strip().split())

    if l * 2 <= r:
        print(l, l*2)
    else:
        print(-1, -1)
