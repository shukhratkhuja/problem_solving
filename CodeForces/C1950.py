import sys

t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):

    hours, minutes = map(int, sys.stdin.readline().strip().split(":"))

    if hours == 12:
        results.append(":".join(['12', str(minutes).zfill(2)])+ ' PM')
    elif hours == 0:
        results.append(":".join(['12', str(minutes).zfill(2)])+ ' AM')
    elif hours > 12:
        results.append(":".join([str(hours-12).zfill(2), str(minutes).zfill(2)])+ ' PM')
    else:
        results.append(":".join([str(hours).zfill(2), str(minutes).zfill(2)])+ ' AM')

sys.stdout.write("\n".join(results) + "\n")
