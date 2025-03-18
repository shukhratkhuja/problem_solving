name = input()

print("CHAT WITH HER!" if len(set([c for c in name]))%2==0 else "IGNORE HIM!")