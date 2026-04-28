# Problem: Sum of Two Values
# Contest: CSES - CSES Problem Set
# URL: https://cses.fi/problemset/task/1640
# Memory Limit: 512; Time Limit: 1000
#
# Date: 4/2/2025, 8:58:48 AM

import os
import sys
import math
from itertools import combinations

dprint = lambda *args, **kwargs: DEBUG and print(
    "DEBUG:", *args, file=sys.stderr, **kwargs
)


def main(problem_name=None):
    if os.path.exists(f"{problem_name}.in"):
        sys.stdin = open(f"{problem_name}.in", "r")
        sys.stdout = open(f"{problem_name}.out", "w")

    n,s = tuple(map(int, input().split()))
    nums = list(map(int, input().split()))

    seen = set()
    for i , num in enumerate(nums):
        if num in seen:
            print(nums.index(s-num) + 1, i + 1)
            return

        seen.add(s-num)
    print("IMPOSSIBLE")

if __name__ == "__main__":
    DEBUG = False
    main("")