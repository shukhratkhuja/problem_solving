from itertools import combinations

word, n = input().split()
l = []
for i in range(1, int(n)+1):
    l1 = map(sorted, combinations(word, i))
    ll = sorted(list(map(''.join, l1)))
    for v in ll:
        print(v)

    