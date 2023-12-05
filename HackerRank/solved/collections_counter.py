from collections import Counter, defaultdict

shoes = int(input())

sizes = list(map(int, input().split()))
sizes = defaultdict(Counter(sizes))

customers = int(input())
size_cost = []

summ = 0
for i in range(customers):
    size, cost = map(int, input().split())
    if sizes[size] > 0:
        summ += cost
        sizes[size] -= 1

print(summ)
