a = input().split(" ")
b = input().split(" ")

x = [int(i) for i in a]
y = [int(i) for i in b]

y.sort()

numcoins = x[0]
target = x[1]
coins = y

dp = []
for i in range(target+1):
    dp.append(1000001)
dp[0] = 0

for num in coins:
    if target > num:
        dp[num] = 1

for i in range(1, target+1):
    for j in range(numcoins):
        if i - coins[j] >= 0:
            if dp[i-coins[j]] + 1 < dp[i]:
               dp[i] = dp[i-coins[j]] + 1
if dp[target] == 1000001:
    dp[target] = -1

print(dp[target])
