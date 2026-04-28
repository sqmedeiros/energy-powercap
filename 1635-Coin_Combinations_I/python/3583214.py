from sys import stdin, stdout

# from heapq import heapify, heappush, heappop
# import math

mod = 1000000007

#
# # mod9 = 9
# # fact = []
# # permute = []
#
#
# def decimalToBinary(n):
#     return bin(n).replace("0b", "")
#
#
# def binaryToDecimal(n):
#     return int(n, 2)
#
#
# def buildFact(n, m):
#     fact.append(1)
#     for i in range(1, n + 1):
#         fact.append(fact[-1] * i)
#         fact[-1] %= m
#     return fact
#
#
# def buildSieve(n):
#     prime = [True for i in range(n + 1)]
#     p = 2
#     while p * p <= n:
#         if prime[p]:
#             for i in range(p * p, n + 1, p):
#                 prime[i] = False
#         p += 1
#     return prime
#
#
# def findDivisors(n):
#     i = 1
#     arr = []
#     while i * i < n:
#         if n % i == 0:
#             arr.append(i)
#         i += 1
#     m = int(math.sqrt(n))
#     for i in range(m, 0, -1):
#         if n % i == 0:
#             arr.append(n // i)
#     return arr
#
#
# def findPermutation(n, arr, ans):
#     if len(arr) == n:
#         ans.append(arr)
#     ar = [i for i in arr]
#     ar.append(0)
#     for i in range(1, n + 1):
#         if i not in ar:
#             ar[-1] = i
#             findPermutation(n, ar, ans)


# stdin.readline()      map(int, stdin.readline().split())


# def solve():
n, x = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
dp = [0 for i in range(x+1)]
dp[0] = 1
for i in range(1, x + 1):
    for j in arr:
        if j <= i:
            dp[i] += dp[i - j]%mod
print(dp[x] % mod)
    # return


#   MAIN FUNCTION
# tests = int(stdin.readline())
# tests = 1
# for _ in range(tests):
#     solve()