n, k = map(int, input().split())
scores = list(map(int, input().split()))

result = len([i for i in scores if i != 0 and i >= scores[k-1]])
print(result)