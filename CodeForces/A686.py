import sys

t, x = map(int, sys.stdin.readline().strip().split())
d = 0

for _ in range(t):
    sign, pcount = sys.stdin.readline().strip().split()
    pcount = int(pcount)

    if sign == '-' and pcount <= x:
        x -= pcount
    elif sign == '-' and pcount > x:
        d += 1
    else:
        x += pcount

print(x, d)