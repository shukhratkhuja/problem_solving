n, k = map(int, input().split())
scores = list(map(int, input().split()))
partisipants = 0

for i in range(0,n):
    if scores[i] == 0:
        print(partisipants)
        break
    elif i <= k-1:
        partisipants += 1
    elif scores[i] == scores[i-1]:
        partisipants += 1
    else:
        print(partisipants)
        break
else:
    print(partisipants)
