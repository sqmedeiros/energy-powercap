number, value = map(int, input().split()) #different value types 
coins_list = list(map(int, input().split()))

INF = 10**9
dp =[INF]*(value+1)
dp[0] = 0 

for coin in coins_list:
    for amount_left in range(1, value+1):
        if coin <= amount_left:
            dp[amount_left] = min(dp[amount_left], (dp[amount_left - coin] + 1)) #the catch

print(dp[value] if dp[value] != INF else -1)

