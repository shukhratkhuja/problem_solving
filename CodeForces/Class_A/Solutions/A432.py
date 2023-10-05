n, k = map(int, input().split())
l = map(int, input().split())

ls = list(map(lambda x: x+k, l))
lc = [c for c in ls if c <= 5]
print(len(lc)//3)