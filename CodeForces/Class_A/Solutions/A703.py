n = int(input())
w = 0
for _ in range(n):
    m, c = map(int, input().split())

    if m > c:
        w += 1
    elif m < c:
        w -= 1

if w > 0:
    print('Mishka')
elif w < 0:
    print('Chris')
else:
    print('Friendship is magic!^^')
