t = int(input())

for _ in range(t):
    c = int(input())
    if c % 3 == 1:
        print(c // 3 + 1, c // 3)
    elif c % 3 == 2:
        print(c // 3, c // 3 + 1)
    else:
        print(c // 3, c // 3)
