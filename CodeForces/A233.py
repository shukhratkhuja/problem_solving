import sys

n = int(sys.stdin.readline().strip())
#my solution
# if n % 2 == 0:
#     answer = [i + 2 if i % 2 == 0 else i for i in range(n) ]
# else:
#     answer = [-1]

# gpt solution
answer = []
if n % 2 == 1:
    sys.stdout.write("-1" + "\n")
else:
    
    for i in range(1, n+1, 2):
        answer.append(i+1)
        answer.append(i)

sys.stdout.write(" ".join(map(lambda x: str(x), answer)) + "\n")
