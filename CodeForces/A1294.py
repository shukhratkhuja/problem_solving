t = int(input())

for i in range(t):
    a, b, c, n = map(int, input().split())
    x = a + b + c + n
    if x % 3 == 0 and (x / 3 >= a and x / 3 >= b and x / 3 >= c):
        print('YES')
    else:
        print('NO')