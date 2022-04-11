#!/bin/python3

import math
import os
import random
import re
import sys

from avl_tree import AVLTree

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    total_bribe_cnt = 0
    tree = AVLTree()
    for i, x in enumerate(q):
        k = tree.values_bigger_than_k(x)
        bribe_cnt = (x - 1 + k) - i
        if bribe_cnt < 0:
            continue
        if bribe_cnt > 2:
            print("Too chaotic")
            return
        total_bribe_cnt += bribe_cnt
        tree.add(x)
    print(total_bribe_cnt)


if __name__ == "__main__":
    with open("input.txt") as f:
        t = int(f.readline().strip())

        for t_itr in range(t):
            n = int(f.readline().strip())

            q = list(map(int, f.readline().rstrip().split()))

            minimumBribes(q)
