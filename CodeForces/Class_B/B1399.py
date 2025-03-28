import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n = int(sys.stdin.readline().strip())
    candies = list(map(int, sys.stdin.readline().strip().split()))
    oranges = list(map(int, sys.stdin.readline().strip().split()))
    
    min_candies = min(candies)
    min_oranges = min(oranges)

    candies_dif = list(map(lambda x: x-min_candies, candies))
    oranges_dif = list(map(lambda x: x-min_oranges, oranges))

    answer = 0
    for i in range(n):
        answer += min(candies_dif[i], oranges_dif[i]) + abs(candies_dif[i] - oranges_dif[i])
    
    results.append(str(answer))

sys.stdout.write("\n".join(results) + "\n")
