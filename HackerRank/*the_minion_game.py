def minion_game(string):
    
    vowels = 'AEIOU'

    vnum = 0
    cnum = 0
    n = len(string)
    
    for i, c in enumerate(string):
        print(n-i)
        if c in vowels:
            vnum += n - i
        else:
            cnum += n - i

    if vnum == cnum:
        print("Draw")
    elif vnum > cnum:
        print("Kevin", vnum)
    else:
        print("Stuard", cnum)


    # dnv = {}
    # dv = {}
    
    # for i in range(1,len(string)+1):
    #     for j in range(len(string)):
    #         if string[j] not in vowels:
    #             if j+i <= len(string):
    #                 if string[j:j+i] in dnv.keys():
    #                     dnv[string[j:j+i]] += 1
    #                 else:
    #                     dnv[string[j:j+i]] = 1
    #         else:
    #             if j+i <= len(string):
    #                 if string[j:j+i] in dv.keys():
    #                     dv[string[j:j+i]] += 1
    #                 else:
    #                     dv[string[j:j+i]] = 1

    # if sum(dnv.values()) > sum(dv.values()):
    #     print("Stuart", sum(dnv.values()))
    # elif sum(dv.values()) > sum(dnv.values()):
    #     print("Kevin", sum(dv.values()))
    # else:
    #     print("Draw")
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)