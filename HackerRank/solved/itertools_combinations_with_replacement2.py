from itertools import combinations_with_replacement

word, n = input().split()

print('\n'.join(''.join(v) for v in  sorted(combinations_with_replacement(sorted(list(word)), int(n)))))
