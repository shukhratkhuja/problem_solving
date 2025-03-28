import sys


input_data = sys.stdin.read().split()

t = int(input_data[0])
index = 1

results = []

for _ in range(t):
    a, b, c = map(int, input_data[index: index + 3])
    index += 3

    if c % 2 == 1:
        if a >= b:
            results.append("First")
        else:
            results.append("Second")
    else:
        if a > b:
            results.append("First")
        else:
            results.append("Second")
        
sys.stdout.write("\n".join(results) + "\n")
