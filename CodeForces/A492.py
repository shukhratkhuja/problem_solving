import sys

n = int(sys.stdin.readline().strip())

height = 0
total_cubes = 0
total_cubess = []
i = 1
while total_cubes + i*(i+1) // 2 <= n:
    total_cubes += i*(i+1) // 2
    height += 1
    i+=1

sys.stdout.write(str(height))
