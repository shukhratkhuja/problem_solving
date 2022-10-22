n, m = map(int, input().split())

for column in range(n):
    
    if n // 2 == column:
        un = '---' * ((n - 3) // 2)
        print(f"{un}-WELCOME-{un}")
    elif n // 2  > column:
        pc = (column * 2 + 1)
        pn = '.|.' * pc
        un = '---' * ((n - pc) // 2)
        print(f"{un}{pn}{un}")
    else:
        pc = (column - (n // 2))
        pn = '.|.' * (n - pc * 2)
        un = '---' * (pc)
        print(f"{un}{pn}{un}")
        