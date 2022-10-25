t = int(input())

for test in range(t):
    n = int(input())
    l = 0
    r = 0
    counter = 0
    for i in range(n, 0, -1):
        if i == n or counter >= n / 2:
            # print('i = ', i)
            r += 2 ** i
        else:
            counter+=1
            l += 2 ** i
    print(abs(l-r))   
