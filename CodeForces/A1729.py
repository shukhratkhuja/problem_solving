import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):

    a, b, c = map(int, sys.stdin.readline().strip().split())
    
    sys.stdout.write("\n")
    if c > b:
        if a > c-b+c:
            sys.stdout.write("2")
        elif c-b+c > a:
            sys.stdout.write("1")
        else:
            sys.stdout.write("3")
    else:
        if a > b:
            sys.stdout.write("2")
        elif b > a:
            sys.stdout.write("1")
        else:
            sys.stdout.write("3")

sys.stdout.write("\n")

