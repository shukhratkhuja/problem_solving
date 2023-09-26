n, m = map(int, input().split())
l = ''
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            l += '#'
        else:
            if (i-1) % 4 == 0 and j == m-1:
                l += '#'
            elif j == 0 and (i-1) % 4 != 0:
                l += '#'
            else:
                l += '.'
    l += '\n'
print(l)
