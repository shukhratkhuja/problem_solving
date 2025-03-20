import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):
    
    a = []
    word = ''
    
    for _ in range(8):
        l = sys.stdin.readline().strip()
        a.append(l)
    word = (''.join(a)).replace('.', '')

    results.append(word)


sys.stdout.write("\n".join(results) + "\n")
