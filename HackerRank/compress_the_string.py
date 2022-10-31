from itertools import groupby

S = input()
elements = [(len(list(g)), int(k)) for k, g in groupby(S)]
print(*elements, end=' ')