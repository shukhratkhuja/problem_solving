from itertools import groupby

s = input()
l = []
for key, group in groupby(s):
    l.append((len(list(group)), int(key)))
print(*l)