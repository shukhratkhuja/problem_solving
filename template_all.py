import sys

def solve():
    # Fast input
    
    input_data = sys.stdin.read().split()
    
    t = int(input_data[0])  # Testlar soni
    index = 1

    results = []

    for _ in range(t):
        n = int(input_data[index])  # Array uzunligi
        arr = map(int, input_data[index + 1: index + 1 + n])
        index += 1 + n

        results.append(str())

    # Fast output
    sys.stdout.write("\n".join(results) + "\n")

solve()

