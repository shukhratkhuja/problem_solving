import sys, math

t = int(sys.stdin.readline().strip())
# results = []
for _ in range(t):

    n, m = map(int, sys.stdin.readline().strip().split())

    sys.stdout.write("\n")
    sys.stdout.write(str(math.ceil(m * n / 2)))

sys.stdout.write("\n")
    
    # my solution

    # if m > n:
    #     n, m = m, n
    
    # if n % 2 == 0:    
    #     results.append(str(n//2 * m))
    # else:
    #     results.append(str(n//2 * m + math.ceil(m/2)))


# sys.stdout.write("\n".join(results) + "\n")
