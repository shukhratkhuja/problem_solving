n = int(input())

for i in range(0, 2*n-1):
    for j in range(0, 2*n-1):
        if i+j==0:
            print(i*(2*n-1)+j, end=' ')
    print()



# for i in range(1, 2*n):
#     for j in range(1, 2*n):
#         print(i*(2*n-1)+j, end=' ')
#     print()