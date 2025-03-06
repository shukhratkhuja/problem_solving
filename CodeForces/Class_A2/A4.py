w = int(input())

def watermelon(kg):
    if kg%2==0 and kg > 2:
        return "YES"
    return "NO"

print(watermelon(kg=w))