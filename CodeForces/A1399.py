t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    for i in range(1, n):
        if l[i] - l[i-1] <= 1 and i == n - 1:
            pass
        elif l[i] - l[i-1] > 1:
            print('NO')
            break
    else:
        print('YES')
