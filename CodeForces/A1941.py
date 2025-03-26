import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    n, m, k = map(int,sys.stdin.readline().strip().split())
    
    b = list(map(int, sys.stdin.readline().strip().split()))
    c = list(map(int, sys.stdin.readline().strip().split()))
    
    b.sort()
    c.sort()

    answer = 0
    j = m - 1  # O'ng tomondagi massivning eng katta elementidan boshlaymiz

    # Chap massiv bo‘yicha yuramiz
    for i in range(n):
        while j >= 0 and b[i] + c[j] > k:
            j -= 1  # Juda katta bo‘lsa, `j`ni kamaytiramiz
        
        # Endi `j` gacha bo‘lgan barcha elementlar `b[i] + c[j] ≤ k` shartini qanoatlantiradi
        answer += (j + 1)  


    # my_solution
    # answer = 0
    
    # for i in b:
    #     for j in c:
    #         if i+j <=k:
    #             answer += 1
    #         else:
    #             break

    results.append(str(answer))

sys.stdout.write("\n".join(results) + "\n")
