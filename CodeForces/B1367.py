t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    e = 0
    ei = 0
    for i in range(n):
        
        if i % 2 == 0:
            ei += 1
        
        if l[i] % 2 == 0:
            e += 1
    
    # le = []
    # lei = []
    # lo = []
    # loi = []

    # if ei == e:

    #     for i in range(n):
    #         if l[i] % 2 == 0:
    #             le.append(l[i])
    #             lei.append(i)
    #         else:
    #             lo.append(l[i])
    #             loi.append(i)
    #     path = 0
    #     nl = []
    #     for i in range(n):
    #         if i % 2 == 0:
    #             nl.append(le[i//2])
    #             path += abs(i - lei[i//2])
    #         else:
    #             nl.append(lo[i//2])
    #             path += abs(i - loi[i//2])

        # print("#" * 100)
        # print(nl)
        # print(path//2)
        # print("#" * 100)
    else:
        print(-1)

