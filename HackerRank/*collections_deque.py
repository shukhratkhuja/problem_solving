from collections import deque
"""
append
appendleft
clear
pop
popleft
extend
remove
reverse
rotate (positive number <-, negative number ->)
"""
# dq = deque()
# n = int(input())
# for _ in range(n):
#     command_value = input()
#     if command_value == "pop":
#         dq.pop()
#     elif command_value == "popleft":
#         dq.popleft()
#     else:
#         command, value = command_value.split()
#         if command == "append":
#             dq.append(int(value))
#         elif command == "appendleft":
#             dq.appendleft(int(value))

# print(*dq)
from collections import deque

dq = deque()
for _ in range(int(input())):
    cm = input().split()
    ex = f"dq.{cm[0]}({cm[1]})" if len(cm) == 2 else f"dq.{cm[0]}()"
    eval(ex)
print(*dq)