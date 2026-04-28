def solve(n,total, arr):
    dp = [total+1]*(total+1)
    dp[0] = 0
    for i in range(1,total+1):
        for coin in arr:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)
            else:
                break
    if dp[total] > total:
        print(-1)
    else:
        print(dp[total])

n, total = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
solve(n,total, arr)