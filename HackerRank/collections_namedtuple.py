from collections import namedtuple


n = int(input())
sum_marks = 0
for i in range(n):
    values = {}
    if i == 0:
        columns = input().split()
        Pupil = namedtuple('Pupil', columns)

    values[columns[0]], values[columns[1]], values[columns[2]], values[columns[3]] = input().split()

    p = Pupil(**values)

    sum_marks += int(p.MARKS)

print('%.2f'%(sum_marks/n))
