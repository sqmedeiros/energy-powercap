# n, x=map(int, input().split())
# arr=list(map(int, input().split()))
# dp=[0 for i in range(x+1)]
import sys
M=1000000007
# input=sys.stdin.readline
n, x=[int(i) for i in input().split()]
arr=[int(i) for i in input().split()]
dp=[1]+[0]*x
dp[0]=1
for i in range(x+1):
    if not dp[i]:
        continue
    for j in arr:
        if i+j>x:
            continue
        dp[i+j]=(dp[i+j]+dp[i])%M
print(dp[x])