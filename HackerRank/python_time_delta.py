
import math
import os
import random
import re
import sys
from datetime import datetime, timedelta
import time
# Complete the time_delta function below.
def time_delta(t1, t2):

    format_date = "%a %d %b %Y %X %z"
    ft1 = datetime.strptime(t1, format_date)
    ft2 = datetime.strptime(t2, format_date)
    d = (ft2-ft1).total_seconds()
    
    return '%d'%int(abs(d))
    
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

    #     fptr.write(delta + '\n')

    # fptr.close()
