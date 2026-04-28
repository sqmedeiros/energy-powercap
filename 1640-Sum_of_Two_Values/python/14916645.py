'''
 '''

import sys
import heapq
from math import gcd, ceil, floor
from collections import defaultdict, Counter, deque
from typing import List, Optional, Dict, Tuple

input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(3*10**5)
INF = float("inf")


def solve(n: int, k: int, nums: List[int]) -> Tuple[int, int]:
    n = len(nums)
    hashmap = dict()
    for i in range(n):
        if k - nums[i] in hashmap:
            return i+1, hashmap[k- nums[i]]+1
        hashmap[nums[i]] = i
    return "IMPOSSIBLE"

def solve(n: int, k: int, nums: List[int]) -> Tuple[int, int]:
    n = len(nums)
    arr = [(num, i+1) for i, num in enumerate(nums)]
    arr.sort()
    low = 0
    high = n-1
    while(low < high):
        curr_sum = arr[low][0] + arr[high][0]
        if curr_sum == k:
            return arr[low][1], arr[high][1]
        elif curr_sum < k:
            low += 1
        else:
            high -= 1
    return "IMPOSSIBLE"

def main() -> None:
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    res = solve(n, k, nums)
    if res == "IMPOSSIBLE":
        print(res)
    else:
        print(*res)

if __name__ == "__main__":
    main()