import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n, k = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    b = list(map(int, sys.stdin.readline().strip().split()))
    
    a.sort()
    b.sort()
    
    for i in range(k):
       
        if a[i] < b[-(i+1)]:
            a[i] = b[-(i+1)]

            # print()
            # print("#"*20)
            # print(a)
            # print(b)
            # print("#"*20)
    results.append(str(sum(a)))


sys.stdout.write("\n".join(results) + "\n")
