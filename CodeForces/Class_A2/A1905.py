t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    print(a ^ b ^ c)
    
    # if a == b:
    #     print(c)
    # elif b == c:
    #     print(a)
    # else:
    #     print(b)