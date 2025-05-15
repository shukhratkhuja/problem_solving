import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    s = sys.stdin.readline().strip()
    if len(set(s)) > 1:
        print("YES")
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                r = s[:i-1]+s[i]+s[i-1]+s[i+1:]
                print(r)
                break

    else:
        print("NO")
