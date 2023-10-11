t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    if a < b:
        if 2 * a > b:
            print((a*2)**2)
        else:
            print(b**2)
        
    else:
        if 2 * b > a:
            print((b*2)**2)
        else:
            print(a**2)
