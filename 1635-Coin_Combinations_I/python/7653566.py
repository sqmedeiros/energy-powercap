def solve(x):
    ans = [0] * (x + 1)
    ans[0] = 1

    for p in range(x + 1):
        if ans[p] == 0:
            continue
        for i in coins:
            if i + p <= x:
                ans[i + p] = (ans[i + p] + ans[p]) % 1000000007

    return ans[x]

n, x = map(int, input().split())
coins = list(map(int, input().split()))

print(solve(x))