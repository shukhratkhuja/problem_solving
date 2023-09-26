p, t = map(int, input().split())
lt = 240 - t

s = 0

while True:
    lt -= (s+1) * 5
    if  lt >= 0:
        s += 1
        if s == p:
            break
    else:
        break

print(s)