import sys
data = sys.stdin.read().strip().split()
s = data[0]
t = data[1]
n = len(s)
m = len(t)
INF = 10 ** 9 + 7
# @lru_cache(None)
# def dp(i,j):
#     if i >= n or j >= m:
#         if i >= n:
#             return m-j
#         else:
#             return n-i

#     ans = INF
#     if s[i] != t[j]:
#         add = 1 + dp(i,j+1)
#         rplc = 1 + dp(i+1,j+1)
#         rmv = 1 + dp(i+1,j)
#         ans = min(ans,add,rplc,rmv)
#     else:
#         ans = min(ans,dp(i+1,j+1))
#     return ans
# print(dp(0,0))


dpTable = [[INF for _ in range(m+1)] for _ in range(n+1)]
for i in range(n+1):
    dpTable[i][0] = i
for i in range(m+1):
    dpTable[0][i] = i
for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] == t[j-1]:
            dpTable[i][j] = dpTable[i-1][j-1]
            continue
        add = 1 + dpTable[i][j-1]
        rmv = 1 + dpTable[i-1][j]
        rplc = 1 + dpTable[i-1][j-1]
        dpTable[i][j] = min(dpTable[i][j],add,rmv,rplc)
print(dpTable[n][m])
