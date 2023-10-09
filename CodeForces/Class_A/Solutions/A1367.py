t = int(input())
for _ in range(t):
    b = input()
    nt = b[0]
    for i in range(1, len(b)):
        if i % 2 == 1:
            nt += b[i]
        
    print(nt)
        

