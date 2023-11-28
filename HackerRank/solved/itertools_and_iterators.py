from itertools import combinations, combinations_with_replacement

N = int(input())
letters = input().split()
K = int(input())

combs = list(combinations(range(1,5), 2))
inds = [i for i, letter in enumerate(letters) if letters[K-1] == letter]
print(combs)
print(inds)