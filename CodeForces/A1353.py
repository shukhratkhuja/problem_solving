import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):

    n, m = map(int, sys.stdin.readline().strip().split())
    sys.stdout.write("\n")
    if n == 1:
        sys.stdout.write("0")
    elif n > 2:
        sys.stdout.write(str(2*m))
    else:
        sys.stdout.write(str(m))

sys.stdout.write("\n")

