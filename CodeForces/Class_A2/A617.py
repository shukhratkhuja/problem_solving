x = int(input())
steps = 0

for step in range(5,0,-1):
    step_count = x//step
    steps += step_count
    x -= step * step_count
    
    # print("S", step, "X", x, "C", step_count)

print(steps)