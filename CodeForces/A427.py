n = int(input())
s = map(int, input().split())

res_l = 0
res_r = 0

for i in s:
    if i < 0 and res_r > 0 or i > 0:
        res_r += i
    else:
        res_l += i
    
    # print("RES_L", res_l, "RES_R", res_r)

print(abs(res_l + res_r) if res_r < 0 else abs(res_l))