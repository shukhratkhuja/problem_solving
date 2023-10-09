t = int(input())

for _ in range(t):

    n = int(input())

    if (n / 2) % 2 == 0:
        print('YES')
        l = [i for i in range(n)]
        for i in range(n//2):
            l[i] = i * 2 + 2
            if i == n//2-1:
                l[-(i+1)] = sum(l[:n//2+1]) - sum(l[n//2:])
            else:
                l[-(i+1)] = i * 2 + 1
        print(*l)
    else:
        print('NO')