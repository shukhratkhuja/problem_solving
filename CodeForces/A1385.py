import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):

    x, y, z = map(int, sys.stdin.readline().strip().split())

    if x == y and y == z:
        sys.stdout.write(f"\nYES\n{x} {y} {z}")

    elif x == y and y > z:
        sys.stdout.write(f"\nYES\n{x} {z} 1")
    
    elif x < y and y == z:
        sys.stdout.write(f"\nYES\n{x} 1 {z}")
    
    elif x > y and x == z:
        sys.stdout.write(f"\nYES\n{x} {y} 1")
    
    else:
        sys.stdout.write("\nNO")

sys.stdout.write("\n")
