p, t = map(int, input().split())
q = input()

for i in range(t):
    if 'BG' in q:
        q = q.replace('BG', 'GB')
    
print(q)