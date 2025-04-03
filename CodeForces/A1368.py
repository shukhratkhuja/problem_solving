import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    a, b, n = map(int, sys.stdin.readline().strip().split())

    # gpt
    if a > b:
        a, b = b, a  # a har doim kichikroq bo‘lsin
    answer = 0
    while b <= n:
        a, b = b, a + b
        answer += 1

    # my solution
    # answer = 1
    # while a + b <= n:

    #     if a < b:
    #         a += b
    #     else:
    #         b += a
    #     answer += 1
   
    results.append(str(answer))


sys.stdout.write("\n".join(results) + "\n")
