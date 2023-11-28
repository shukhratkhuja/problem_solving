from itertools import permutations

s, k = input().split()

perms = sorted(list(permutations(s, int(k))))
for i in perms:
    print(''.join(i))
