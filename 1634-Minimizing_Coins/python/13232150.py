n, x = map(int, input().split())
c = list(map(int, input().split()))

"""
Main problem: Find the minimum number of coins that can sum up to x.
Sub problem: Find the mininum number of coins that can sum up to k+c1,k+c2, k+c3 ...... k+cn where k+ci < x and k = 1 to x
Base problem: For sum 0, we can say that minimum number of coins is 0
State: dp[k] Minimum number of coins that sum up to k.
Transition: For any k, minimum number of coins for (k + i) where i is the coins.
 for eg: for n=3 x=11 and coins = [1 5 7]. Minimum number of coins will be 3 that will sum up to 11 (1, 5, 5)
 1 -> 1 + 1 / 1 + 5 / 1 + 7
 1 + 1 = 2 -> 2 + 1 / 2 + 5 / 2 + 7
 1 + 5 = 6 -> 6 + 1 / 6 + 5(11) -> 1 + 5 + 5 Answer
 1 + 7 = 8 -> 8 + 1
 so on ....
 """

dp = [1000000000] * (x + 1)
dp[0] = 0

for i in range(x):
    for coin in c:
        if i + coin <= x:
            dp[i + coin] = min(dp[i + coin], dp[i] + 1)

print(dp[x] if dp[x] != 1000000000 else -1)