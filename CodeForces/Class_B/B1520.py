t = int(input())

for n in range(t):
    n = int(input())
    l = len(str(n))
    x = n // int('1'*l)
    x = (l-1) * 9 + x
    print(x)

