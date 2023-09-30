t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a > b:
        if (a-b)%10 == 0:
            print((a-b)//10)
        else:
            print((a-b)//10+1)
    else:
        if (b-a)%10 == 0:
            print((b-a)//10)
        else:
            print((b-a)//10+1)