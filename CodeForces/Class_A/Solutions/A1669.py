t = int(input())
for score in range(t):
    score = int(input())
    if score >= 1900:
        print('Division 1')
    elif score < 1900 and score >= 1600:
        print('Division 2')
    elif score < 1600 and score >= 1400:
        print('Division 3')
    else:
        print('Division 4')