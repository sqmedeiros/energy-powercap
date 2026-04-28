for _ in range(1):
    # n = int(input())
    m, n = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[0] = 1
    res = 0
    nums.sort()
    mod = 10 ** 9 + 7
    for i in range(n + 1):
        if dp[i] == 0: continue
        for s in nums:
            if i + s <= n:
                dp[i + s] = (dp[i + s] + dp[i]) % mod
                # res += 1

            else:
                break
    # print(dp)
    print(dp[n] % mod if dp[n] else 0)
    # print(res)