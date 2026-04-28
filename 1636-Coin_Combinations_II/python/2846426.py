# # -*- coding: utf-8 -*-
# # @project : 《Atcoder》
# # @Author : created by bensonrachel on 2021/9/15
# # @File : 3.Coin Combinations II.py
#
# modulo = 10**9 + 7
#
# def solve():
#     for i in range(1,n+1):
#         for j in range(1,x+1):
#             if(j<rate[i]):
#                 dp[i][j] = dp[i-1][j]%modulo
#             else:
#                 dp[i][j] = (dp[i-1][j] + dp[i][j-rate[i]])%modulo
#     return dp[-1][-1]%modulo
#
#
# if __name__ == '__main__':
#     n,x = map(int ,input().split())
#     rate = [int(i) for i in input().split()]
#     rate = [0] + rate
#     dp = [[0]*(x+1) for i in range(n+1)]
#     for i in range(n+1):
#         dp[i][0] = 1
#     ans = solve()
#     print(ans)

# -*- coding: utf-8 -*-
# @project : 《Atcoder》
# @Author : created by bensonrachel on 2021/9/15
# @File : 3.Coin Combinations II.py

modulo = 10**9 + 7

def solve():
    for i in range(1,n+1):
        for j in range(rate[i],x+1):
                dp[j] = (dp[j] + dp[j-rate[i]])%modulo
    return dp[-1]%modulo


if __name__ == '__main__':
    n,x = map(int ,input().split())
    rate = [int(i) for i in input().split()]
    rate = [0] + rate
    dp = [0]*(x+1)
    dp[0] = 1
    ans = solve()
    print(ans)
