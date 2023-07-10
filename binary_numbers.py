#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    count = 0
    max = 0
    while n > 0:
        tmp = n % 2
        n //= 2
        if tmp == 1:
            count += 1
            if max < count:
                max = count
        else:
            count = 0
    print(max)
