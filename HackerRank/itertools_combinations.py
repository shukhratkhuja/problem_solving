from itertools import combinations

s, k = input().split()

for l in range(1,int(k)+1):
    print('\n'.join(sorted(''.join(sorted(comb)) for comb in list(combinations(s, l)))))
