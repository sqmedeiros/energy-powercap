import sys
import threading
from math import inf
from functools import lru_cache
input = sys.stdin.readline

############ ---- Input Functions ---- ############
inp = sys.stdin.readline
def input(): return inp().strip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))


def solve():
    s1, s2 = input(), input()
    n, m = len(s1), len(s2)
    """
     @lru_cache(None)
    def dp(i, j):
        if i != n and j == m:
            return n-i
            # return dp(i+1, j) + 1
        if i == n and j != m:
            # return dp(i, j+1) + 1
            return m-j
         if i == n or j == m:
            return 0
         if s1[i] == s2[j]:
            return dp(i+1, j+1)
        add = dp(i, j+1)
        remove = dp(i+1, j)
        replace = dp(i+1, j+1)
        # print(i, j, add, remove, replace)
        return min(add, replace, remove)+1
     return dp(0, 0)
    """
    dp = [[0]*(m+1) for _ in range(n+1)]

    for word1 in range(n):
        dp[word1][-1] = n-word1
    for word2 in range(m):
        dp[-1][word2] = m-word2

    for word1 in range(n-1, -1, -1):
        for word2 in range(m-1, -1, -1):
            if s1[word1] == s2[word2]:
                dp[word1][word2] = dp[word1+1][word2+1]
                continue
            add = dp[word1][word2+1]
            remove = dp[word1+1][word2]
            replace = dp[word1+1][word2+1]

            dp[word1][word2] = min(add, replace, remove)+1
    return dp[0][0]


def main():
    print(solve())


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()