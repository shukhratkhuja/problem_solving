from collections import defaultdict

n, m = map(int, input().split())
A = defaultdict(list)
B = defaultdict(list)
for i in range(n):
    A[input()].append(i+1)


for j in range(m):
    nword = input()
    if A[nword]:
        print(*A[nword])
    else:
        print(-1) 

"""
5 2
a
a
b
a
b
a
b
"""