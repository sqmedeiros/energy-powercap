def func(arr, x):
    dp = [0] * (x + 1)
    dp[0] = 1
    for i in range(x + 1):
        if dp[i] != 0:
            for j in arr:
                if j + i <= x:
                    dp[i + j] = (dp[i + j] + dp[i]) % (10**9 + 7)
    return dp[x]


n, x = map(int, input().split())
arr = [int(x) for x in input().split()]
print(func(arr, x))