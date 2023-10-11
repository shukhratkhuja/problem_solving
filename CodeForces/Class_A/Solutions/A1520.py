t = int(input())

for _ in range(t):
    n = int(input())
    t = input()
    l = [t[0]]
    if n == 1 or n == 2:
            print('YES')
    else:
        for i in range(1,n):
            if t[i] in l and l[i-1] != t[i]:
                print('NO')
                break
            l.append(t[i])
        else:
            print('YES')

