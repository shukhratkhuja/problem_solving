n = int(input())
s = list(map(int, input().split()))
q = ''
for i, p in enumerate(s):
    q += str(s.index(i+1)+1)
    q += ' '
    
print(q.strip())