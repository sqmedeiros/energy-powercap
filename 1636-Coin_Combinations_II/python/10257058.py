# Read input
import sys
input = sys.stdin.read
#sys.setrecursionlimit(10**6)
data = input().split()

n = int(data[1])
coins= list(map(int, data[2:]))

MOD = 10**9 + 7
#from collections import defaultdict, deque
dp = [0]*(n+1)
dp[0] = 1
for val in coins:
    for i in range(val,n+1):        
        dp[i] = (dp[i]+dp[i-val])% MOD
            #print(i-val,"*",dp[i],dp[i-val])
    #print(i,dp)
print(dp[n])