#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    arr = []
    max = - sys.maxsize - 1

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(4):
        for j in range(4):
            small_square = [arr[i:i+3][k][j:j+3] for k in range(3)]
            sum_small_square = sum([sum(elem) for elem in small_square])
            sum_hour_glass = sum_small_square - small_square[1][0] - small_square[1][2]
            if sum_hour_glass > max:
                max = sum_hour_glass
    print(max)