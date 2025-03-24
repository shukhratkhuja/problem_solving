import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):
    
    # a = []
    # for _ in range(4):
    #     a.append(list(map(int, sys.stdin.readline().strip().split())))
    # a.sort()
    # answer = (a[3][0]-a[0][0]) * a[1][1]-a[0][1]

    xl= []
    yl = []
    for _ in range(4):
        
        x, y = map(int, sys.stdin.readline().strip().split())
        
        xl.append(x)
        yl.append(y)
    
    answer = (max(xl)-min(xl)) * (max(yl)-min(yl))

    results.append(str(answer))

sys.stdout.write("\n".join(results) + "\n")