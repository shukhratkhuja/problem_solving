n = int(input())
k = 0
for c in [100, 20, 10, 5, 1]:
    k += n // c
    n %= c

print(k)
