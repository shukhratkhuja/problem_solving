t = int(input())

def findThief(n: int, l: list) -> int:
    for i in range(2, n+1):
        if l[i-2] == l[i-1]:
            if l[i-1] != l[i]:
                    return i
            else:
                continue
        else:
            if l[i-1] == l[i]:
                return i-2
            else:
                return i-1

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(findThief(n, l)+1)

    