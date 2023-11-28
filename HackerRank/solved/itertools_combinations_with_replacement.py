from itertools import combinations_with_replacement

s, k = input().split()

print('\n'.join(sorted(''.join(sorted(comb)) for comb in list(combinations_with_replacement(s, int(k))))))
