t = int(input())

for _ in range(t):

    x, y, n = map(int, input().split())

    zz = (n - y) // x
    print(zz*x+y)