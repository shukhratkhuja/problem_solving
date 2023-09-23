n = int(input())
s = list(map(int, input().split()))

mxi = s.index(max(s))
s.reverse()
mni = n - s.index(min(s)) - 1

if mxi > mni:
    print(mxi + (n - mni - 2))
else:
    print(mxi + n -1 - mni)