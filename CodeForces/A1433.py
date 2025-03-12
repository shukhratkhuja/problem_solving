import sys

def calculate_sum(number):
    d = number % 10
    result = (d-1) * 10 + sum(range(len(str(number))+1))
    return result

t = int(sys.stdin.readline().strip())
results = []

for _ in range(t):
    x = int(sys.stdin.readline().strip())
    # print(calculate_sum(x))
    results.append(str(calculate_sum(x)))

sys.stdout.write("\n".join(results) + "\n")