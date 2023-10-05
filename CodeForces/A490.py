n = int(input())
l = input()
l = l.replace(' ', '')

d = {1: [], 2: [], 3: []}
for i in range(n):
    d[int(l[i])].append(i+1)
k = min(len(d[1]), len(d[2]), len(d[3]))
print(k)
for i , j, k in zip(d[1], d[2], d[3]):
    print(i, j, k)


