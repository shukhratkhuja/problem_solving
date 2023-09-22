n = int(input())
l = []
for i in range(n):
    if i % 2 == 0:
        l.append('I hate')
    else:
        l.append('I love')

result = ' that '.join(l)
print(result + ' it')
