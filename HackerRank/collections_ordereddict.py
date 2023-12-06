from collections import OrderedDict

ordered_dictionary = OrderedDict()
n = int(input())

for _ in range(n):
    
    *key, value = input().split()
    key = ' '.join(key)
    
    if key not in ordered_dictionary.keys():
        ordered_dictionary[key] = int(value)
    else:
        ordered_dictionary[key] += int(value)

for key, value in ordered_dictionary.items():
    print(key, value)


"""
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
"""