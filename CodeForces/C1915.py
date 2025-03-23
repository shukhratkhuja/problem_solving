import sys, math

def solve():
    # Fast input
    
    input_data = sys.stdin.read().split()
    
    t = int(input_data[0])  # Testlar soni
    index = 1

    results = []

    for _ in range(t):
        n = int(input_data[index])  # Array uzunligi
        a = sum(map(int, input_data[index + 1: index + 1 + n]))
        index += 1 + n

        if math.isqrt(a)**2 == a:
            results.append("YES")
        else: results.append("NO")

    # Fast output
    sys.stdout.write("\n".join(results) + "\n")

solve()




#  import sys, math

# t = int(sys.stdin.readline().strip())
# results = []
# for _ in range(t):

#     n = int(sys.stdin.readline().strip())
#     a = sum(map(int, sys.stdin.readline().strip().split()))
    
    
#     if math.isqrt(a)**2 == a:
#         results.append("YES")
#     else: results.append("NO")

# sys.stdout.write("\n".join(results) + "\n")
