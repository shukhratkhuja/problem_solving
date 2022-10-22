# Number of test cases
t = int(input())

for i in range(t):
    # Length of the sequence
    n = int(input())
    # Sequence
    s = list(map(int, input().split()))
    
    for k in range(len(s)):
        if k % 2 == 0:
            print(s[k//2], end=' ')
        else:
            print(s[len(s)-int(((k+1)//2))], end=' ')
