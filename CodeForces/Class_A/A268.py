n = int(input())

result = 0
teams = []
for _ in range(n):
    teams.append(tuple(map(int, input().split())))

# print(teams)

for i in range(n-1):
    for j in range(i+1, n):
        
        if teams[i][0] == teams[j][1]:
            result += 1
        if teams[j][0] == teams[i][1]:
            result += 1
        # print(teams[i], "=", teams[j])

print(result)