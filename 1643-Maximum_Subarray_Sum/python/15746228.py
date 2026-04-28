import sys
from collections import defaultdict

input = sys.stdin.readline
INF = 10**18


def max_subarray_sum():
    n = int(input())
    arr = [int(x) for x in input().split()]

    max_sum = -INF
    cur_sum = 0

    for x in arr:
        cur_sum = max(x, cur_sum + x)
        max_sum = max(max_sum, cur_sum)

    print(max_sum)


if __name__ == "__main__":
    max_subarray_sum()