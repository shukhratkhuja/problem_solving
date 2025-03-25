import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    xor_sum = ord('A') ^ ord('B') ^ ord('C')
    for _ in range(3):
        s = sys.stdin.readline().strip()

        for c in s:
            if c != '?':
                xor_sum ^= ord(c)
    results.append(chr(xor_sum))

        # if '?' in s:
            # results.append((({'A','B','C'}-set(s))).pop())

sys.stdout.write("\n".join(results) + "\n")