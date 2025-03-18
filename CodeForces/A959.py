import sys

n = int(sys.stdin.readline().strip())

sys.stdout.write("Ehab\n" if n % 2 == 1 else "Mahmoud\n")
