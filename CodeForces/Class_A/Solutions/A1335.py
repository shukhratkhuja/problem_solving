n = int(input())

for _ in range(n):
    k = int(input())

    if k % 2 == 0:
        print((k-2)//2)
    else:
        print(k//2)