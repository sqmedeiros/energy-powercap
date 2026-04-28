import math
import sys
from collections import deque, Counter, defaultdict
from bisect import *
import heapq

MAXN = 2 * int(1e5)
MOD = int(1e9 + 7)
INF = 10**15

def solution() -> None:
 input = sys.stdin.readline
 s1 = input().strip()
 s2 = input().strip()

 n, m = len(s1), len(s2)

 dp = [[0] * (m+1) for _ in range(n+1)]
 dp[0][0] = 0
 for i in range(1, n+1):
  dp[i][0] = i
 for j in range(1, m+1):
  dp[0][j] = j

 for i in range(1, n+1):
  for j in range(1, m+1):
   if s1[i-1] != s2[j-1]:
    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
   else:
    dp[i][j] = dp[i-1][j-1]

 print(dp[-1][-1])
 # print(*dp, sep='\n')

if __name__=="__main__":
 solution()