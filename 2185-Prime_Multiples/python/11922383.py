from typing import *
import math
import inspect
import random as ___RANDOM___
from collections import *
import copy as ___COPY___
from functools import cmp_to_key

def mrand(begin: Union[int, float], end: Union[int, float]) -> Union[int, float]:
    if isinstance(begin, int) and isinstance(end, int):
        return ___RANDOM___.randint(begin, end)  # Inclusive range for integers
    elif isinstance(begin, float) or isinstance(end, float):
        return ___RANDOM___.uniform(begin, end)  # Inclusive range for floats

    raise ValueError("Both arguments must be either int or float.")

def get_unique(arr: List[Any], compare: Callable[[Any, Any], bool] = None) -> None:
    if compare is None:
        compare = lambda a, b: (a > b) - (a < b)
    arr.sort(key=cmp_to_key(compare))
    new_size = 0
    for i in range(len(arr)):
        if not i or compare(arr[i], arr[i - 1]):
            arr[new_size] = arr[i]
            new_size += 1
    arr[:] = arr[:new_size]
    return arr

def copy(data):
    return ___COPY___.deepcopy(data)

def fill(arr_dims: List[int], set_val: Any = 0) -> List:
    def dfs(i: int) -> List:
        return [dfs(i + 1) if i < len(arr_dims) - 1 else copy(set_val) for _ in range(arr_dims[i])]
    return dfs(0)

def memset(arr: List, set_val: Any = 0, max_depth: int = -1) -> List:
    def dfs(now: List, cur_depth: int):
        for i in range(len(now)):
            if not isinstance(now[i], list) or cur_depth == max_depth:
                now[i] = copy(set_val)
            else:
                dfs(now[i], cur_depth + 1)
    dfs(arr, 0)
    return arr



n, k = map(int, input().split())
nums = list(map(int, input().split()))

boxes = [0] * (k + 1)
for mask in range(1, 1 << k):
    L = 1
    for i in range(k):
        if ((1 << i) & mask) != 0:
            L *= nums[i]
            if L > n:
                break
    boxes[bin(mask).count('1')] += n // L;

ans = 0
for b in range(1, k + 1):
    if b % 2 == 0:
        ans -= boxes[b]
    else:
        ans += boxes[b]

print(ans)