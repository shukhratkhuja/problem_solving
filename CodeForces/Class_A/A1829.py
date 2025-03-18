def differences(word):
    result = 0
    for i, j in zip('codeforces', word):
        if i != j:
            result += 1
    return result

n = int(input())

for _ in range(n):
    word = input()
    print(differences(word))