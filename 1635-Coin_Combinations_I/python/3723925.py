# def checkMaze(num,x,y):
#     path = 0
#     if x>=m-1 and y>=n-1:path += 1
#     elif x>=m-1:path += (checkMaze(num,x,y+1) if num[x][y+1] else 0)
#     elif y>=n - 1: path += (checkMaze(num, x+1, y) if num[x+1][y] else 0)
#     elif num[x+1][y] and num[x][y+1]:path += checkMaze(num, x+1, y) + checkMaze(num, x, y+1)
#     elif num[x+1][y]:path+= checkMaze(num, x+1, y)
#     elif num[x][y+1]:path+= checkMaze(num, x, y+1)
#     return path
#
# # num = [[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
# # print(checkMaze(num,0,0))
# # v = {'d':1,'e':2,'f':3}
# # m,n = len(num),len(num[0])
#
#
# # C-Vacation
# # def fun(n,i):
# #     if n==0:return 0
# #     if dp[n][i]!=-1:return dp[n][i]
# #     dp[n][i] = max(nums[n-1][i]+fun(n-1,(i+1)%3), nums[n-1][i]+fun(n-1,(i+2)%3))
# #     return dp[n][i]
# #
# # n = int(input())
# # dp = [[-1 for i in range(8)] for j in range(100005)]
# # nums = [list(map(int,input().split())) for _ in range(n)]
# # print(max(fun(n,0),fun(n,1),fun(n,2)))
#
# # def fun(n,w):
# #     if n==0 or w==0:return 0
# #     if dp[n][w]!=-1:return dp[n][w]
# #     if nums[n-1][0]<=w:dp[n][w] = max(nums[n-1][1]+fun(n-1,w-nums[n-1][0]),fun(n-1,w))
# #     else: dp[n][w] = fun(n-1,w)
# #     return dp[n][w]
#
# n,w = map(int,input().split())
# nums = []
# MAX = 1000000005
# for i in range(n):nums.append(list(map(int,input().split())))
# dp = [[MAX for i in range(100005)] for j in range(n+1)]
# dp[0][0] = 0
# # for i in dp:print(dp)
# for i in range(1,n+1):
#     for j in range(100005):
#         if nums[i-1][1]>j:dp[i][j] = dp[i-1][j]
#         else: dp[i][j] = min(nums[i-1][0]+dp[i-1][j-nums[i-1][1]],dp[i-1][j])
# for i in range(100004,-1,-1):
#     if dp[n][i]<=w: print(i);break

x,n = map(int,input().split())
MOD = 1000000007
dp = [1]+[0]*n
coins = list(map(int,input().split()))
for i in range(1,n+1):
    for j in coins:
        if i>=j:dp[i] += dp[i-j]%MOD
print(dp[n]%MOD)