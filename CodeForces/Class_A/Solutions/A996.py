n = int(input())
k = 0
for c in [100, 20, 10, 5, 1]:
    k += n // c
    if n == 0:
        break
    n %= c

print(k)
