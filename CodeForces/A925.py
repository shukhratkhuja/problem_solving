import sys, math

#gpt solution
n = int(sys.stdin.readline().strip())
count = 0

for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        count += 1  # i bo‘luvchi
        if i != n // i:
            count += 1  # n / i ham bo‘luvchi

sys.stdout.write(str(count - 1) + "\n") 


# my solution
# n = int(sys.stdin.readline().strip())
# i = 2
# answer = {1}
# while True:
#     if n % i == 0 and n // i not in answer:
#         answer.add(i)
#         answer.add(n // i)
#     elif n // i in answer:
#         break
#     i += 1

# sys.stdout.write(str(len(answer)) + "\n")
