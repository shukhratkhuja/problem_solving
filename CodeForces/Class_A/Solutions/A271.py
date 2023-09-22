year = int(input())
nyear = year
while True:
    nyear+=1
    lod = set([int(x) for x in str(nyear)])

    if len(lod) >= len(str(year)):
        print(nyear)
        break


