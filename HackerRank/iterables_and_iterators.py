from itertools import combinations
from collections import defaultdict

n = int(input())
l = input().split()
k = int(input())

# A = defaultdict(list)
# for i in range(n):
#     if l[i] == 'a':
#         A['a'].append(i+1)
# cmbns = list(combinations(range(1, n+1), k))
# p = 0
# for t in cmbns:
#     for i in A['a']:
#         if i in t:
#             p+=1
#             break

p = 0
cmbns = list(combinations(l, k))
for c in cmbns:
    if 'a' in c:
        p+=1

print('%.9f'%(p/len(cmbns)))
