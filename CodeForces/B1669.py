import sys
from collections import defaultdict

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

        freq = defaultdict(int)

        ans = -1
        for num in arr:
            freq[num] += 1
            if freq[num] == 3:  # Uchinchi marta chiqsa darhol to'xtaymiz
                ans = num
                break

        results.append(str(ans))

    # Fast output
    sys.stdout.write("\n".join(results) + "\n")

solve()


# import sys, collections

# t = int(sys.stdin.readline().strip())
# results = []
# for _ in range(t):

#     n = int(sys.stdin.readline().strip())
#     a = list(map(int, sys.stdin.readline().strip().split()))
    
#     answer = '-1'
#     adict = collections.Counter(a)
#     max_elem, chastota = adict.most_common(1)[0]
#     if chastota > 2:
#         answer = str(max_elem)
    
#     results.append(answer)

# sys.stdout.write("\n".join(results) + "\n")
