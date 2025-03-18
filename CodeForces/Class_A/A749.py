import sys

n = int(sys.stdin.readline().strip())
results = (['2'] * (n // 2)) if n % 2 == 0 else (['2'] * (n // 2 - 1) + ['3'])
sys.stdout.write(str(len(results))+"\n" + " ".join(results)+"\n")
