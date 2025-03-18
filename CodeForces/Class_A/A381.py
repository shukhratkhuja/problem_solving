n = int(input())
l = list(map(int, input().split()))

s, d = 0, 0

for i in range(n):
    if l[-1] > l[0]:
        if i % 2 == 0:
            s += l[-1]
        else:
            d += l[-1]
        del l[-1]
    else:
        if i % 2 == 0:
            s += l[0]
        else:
            d += l[0]
        del l[0]
        
print(s, d)
