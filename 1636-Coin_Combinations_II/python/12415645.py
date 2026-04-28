n,x = map(int, input().split())
coins = list(map(int, input().split()))

dp= [0]*(x+1)
dp[0]= 1 
overflow= 10**9+ 7

coins.sort()
for c in coins: 
    for i in range(c, x+1):  
        if c<=i:
            dp[i]+= dp[i-c]
        dp[i]%=overflow

print(dp[x])