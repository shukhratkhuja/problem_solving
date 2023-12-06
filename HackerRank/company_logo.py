import math
import os
import random
import re
import sys


from collections import Counter, OrderedDict


if __name__ == '__main__':
    s = input()
    
    od = OrderedDict(Counter(s))
    sorted_dict = OrderedDict(sorted(od.items(), key=lambda x: (-x[1], x[0])))
    counter = 1
    for key, value in sorted_dict.items():
        print(key, value)
        if counter == 3: break; counter += 1

                