# import sys
# sys.setrecursionlimit(10**8)
# input = sys.stdin.readline
# from heapq import heappush, heappop, heapify, heappushpop
# from functools import lru_cache

# ONLINE_JUDGE = False
# def debug(*args):
#     if ONLINE_JUDGE:
#         return
#     import inspect
#     frame = inspect.currentframe().f_back
#     line_no = inspect.getframeinfo(frame).lineno 
#     line = inspect.getframeinfo(frame).code_context[0].strip()
#     call = line[line.find('debug(') + 6: line.rfind(')')]
#     var_names = [v.strip() for v in call.split(',')]
#     parts = [f"{name} = {val}" for name, val in zip(var_names, args)]
#     print(f"{line_no}: [" + " || ".join(parts) + "]", file=sys.stderr)


# def solve2():
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     arr = [False] * (n + 1)
#     ans = 0
#     for x in a:
#         for i in range(x, n + 1, x):
#             if arr[i] == False:
#                 print(i, end=" ", file=sys.stderr) 
#                 arr[i] = True
#         print("\n--", file=sys.stderr)
#     for i in range(n + 1):
#         if arr[i]:
#             ans += 1
#     print(ans)
# def solve():
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     ans = 0
#     for x in a:
#         ans += n // x
#     for mask in range(1, 1 << k):
#         curr = 1
#         cnt = 0
#         for i in range(k):
#             if mask & (1 << i):
#                 cnt += 1
#                 curr *= a[i]
#                 if curr > n:
#                     break
#         if cnt != 1:
#             ans -= n // curr
#     print(ans)


# if __name__ == "__main__":
#     T = 1

#     for t in range(1, T + 1):
#         if T != 1 and not ONLINE_JUDGE:
#             print("\n______Test :", t, "\n", file=sys.stderr)
#         solve2()

import sys, math
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
from heapq import heappush, heappop, heapify, heappushpop
from functools import lru_cache

ONLINE_JUDGE = True
def debug(*args):
    if ONLINE_JUDGE:
        return
    import inspect
    frame = inspect.currentframe().f_back
    line_no = inspect.getframeinfo(frame).lineno 
    line = inspect.getframeinfo(frame).code_context[0].strip()
    call = line[line.find('debug(') + 6: line.rfind(')')]
    var_names = [v.strip() for v in call.split(',')]
    parts = [f"{name} = {val}" for name, val in zip(var_names, args)]
    print(f"{line_no}: [" + " || ".join(parts) + "]", file=sys.stderr)


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0 for _ in range(k + 1)]
    for mask in range(1, 1 << k):
        curr = 1
        bitCount = 0
        for i in range(k):
            if mask & (1 << i):
                bitCount += 1
                curr *= a[i]
        dp[bitCount] += n // curr
    def cnt(i):
        return math.comb(k, i)
    def f(j, i):
        return math.comb(k-i, k-j)
    for i in range(k-1, 0, -1):
        for j in range(i + 1, k + 1):
            dp[i] -= dp[j] * f(j, i) * cnt(i) // cnt(j)                
    print(sum(dp))

if __name__ == "__main__":
    T = 1
    for t in range(1, T + 1):
        if T != 1 and not ONLINE_JUDGE:
            print("\n______Test :", t, "\n", file=sys.stderr)
        solve()