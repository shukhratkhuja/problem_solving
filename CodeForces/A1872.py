import sys, math

t = int(sys.stdin.readline().strip())
for _ in range(t):

    a, b, c = map(int, sys.stdin.readline().strip().split())
    
    sys.stdout.write(str(math.ceil(abs(b-a)/2/c)))
    sys.stdout.write("\n")

