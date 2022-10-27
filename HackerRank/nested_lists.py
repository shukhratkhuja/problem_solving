if __name__ == '__main__':
    clas = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        clas.append([name, score])

    scores = set([st[1] for st in clas])
    scores = sorted(list(scores))
    second_lowest = scores[1]
    names = []
    for st in clas:
        if st[1] == second_lowest:
            names.append(st[0])

    for name in sorted(names):
        print(name)

    