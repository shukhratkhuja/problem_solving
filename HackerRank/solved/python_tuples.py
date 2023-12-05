# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
t = input()
t = tuple(map(int, t.split()))
print(hash(t))