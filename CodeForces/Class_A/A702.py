import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

maxl = 1
sub_maxl = 1
for i in range(1, n):
    if a[i-1] < a[i]:
        sub_maxl += 1
    else:
        maxl = max(maxl, sub_maxl)
        sub_maxl = 1

maxl = max(maxl, sub_maxl)
sys.stdout.write(str(maxl) + "\n")
