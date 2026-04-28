n = int(input())
arr = [int(x) for x in input().split()][:n]

prefSum = [0] * (n + 1)
prefMin = [0] * (n + 1)
for i in range(1, n + 1):
    prefSum[i] = prefSum[i-1] + arr[i - 1]
    prefMin[i] = min(prefMin[i-1], prefSum[i])

ans = -10 ** 10
for i in range(1, n + 1):
    ans = max(ans, prefSum[i] - prefMin[i-1])

print(ans)