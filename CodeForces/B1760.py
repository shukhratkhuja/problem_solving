import sys, math

t = int(sys.stdin.readline().strip())
results = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(t):

    max_alpha = 0
    
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()

    #1 solution 
    # sl = [c for c in s]
    # sl.sort()
    # max_alpha = alphabet.index(sl[-1])
    #2 solution
    # for c in s:
    #     if alphabet.index(c) > max_alpha:
    #         max_alpha = alphabet.index(c)
        
    results.append(str(ord(max(s)) - ord('a') + 1)) # GPT solution using ASCII finding the letter with max index from word


sys.stdout.write("\n".join(results) + "\n")
