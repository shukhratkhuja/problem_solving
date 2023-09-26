n = int(input())
scores = list(map(int, input().split()))

mx = scores[0]
mn = scores[0]
cr = 0
for sc in scores:
    if sc > mx:
        cr += 1
        mx = sc
    elif sc < mn:
        cr += 1
        mn = sc

print(cr)
