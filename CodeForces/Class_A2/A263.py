h_index = 0
v_index = 0

for i in range(5):
    s = input()
    if '1' in s:
        h_index = s.find('1') // 2 # because of white spaces in string input
        v_index = i

print(abs(h_index-2)+abs(v_index-2))