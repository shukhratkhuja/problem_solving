import sys

t = int(sys.stdin.readline().strip())
a = [[0]*t]*t

for i in range(t):
    for j in range(t):
        if i == 0 or j == 0:
            a[i][j] = 1
        else:
            a[i][j] = a[i-1][j]+a[i][j-1]
print(a[t-1][t-1])