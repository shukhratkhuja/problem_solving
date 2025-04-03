import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n, k = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))    

    taken = 0
    given = 0
    # print("#"*100)
    for i in a:
        if i >= k:
            taken += i
        elif i == 0 and taken > 0:
            given += 1
            taken -= 1
        # print("GIVEN: ", given)     
        # print("TAKEN: ", taken)     
    # print("#"*100)
    results.append(str(given))
sys.stdout.write("\n".join(results) + "\n")
