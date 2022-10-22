# Number of test cases
t = int(input())

for i in range(t):
    # Length of the sequence
    n = int(input())
    # Sequence
    s = list(map(int, input().split()))
    
    indicator = 0
    for j in range(n):
        if j%2 == 1:
            indicator+=1
        else:
            indicator+=1
    if sum(s) % 2 == 1 or indicator == 2:
        print('YES')
    else:
        print('NO')
