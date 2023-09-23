n = int(input())
for i in range(n):
    r, d = map(int, input().split())

    if r % d == 0:
        print(0)
    else:
        print(((r//d)+1) * d - r)
