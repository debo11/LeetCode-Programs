import numpy as np
import pandas as pd


def findCenter(input1):
    res = list(set.intersection(*map(set, input1)))
    for i in res:
        print(i)


input1 = [[1, 2], [2, 3], [4, 2]]
findCenter(input1)