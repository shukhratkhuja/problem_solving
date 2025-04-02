import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = list(range(1, n+1))
    
    # Har bir 2 ta elementni o'rnini almashtiramiz
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    
    # Agar n toq bo'lsa, oxirgi element o'z o'rnida qoladi, bu xato
    # Shu sababli oxirgi uch elementni aylantiramiz
    if n % 2 == 1:
        arr[-1], arr[-2] = arr[-2], arr[-1]

    sys.stdout.write(' '.join(map(str, arr))+"\n")

