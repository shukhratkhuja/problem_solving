n = int(input())
l = list(map(int, input().split()))

print(sum(list(map(lambda x: max(l)-x, l))))