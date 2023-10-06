t = int(input())

for _ in range(t):
    l = list(map(int, input().split()))
    ls = l.copy()
    ls.sort()

    x = ls.index(l[0])
    print(3-x)

