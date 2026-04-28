n = int(input())

a = list(map(int, input().split()))

pre = [0] * (n + 1)

for i in range(n):
    pre[i + 1] = pre[i] + a[i]

max_sum = float('-inf')
min_prefix = 0

for i in range(1, n + 1):
    max_sum = max(max_sum, pre[i] - min_prefix)
    min_prefix = min(min_prefix, pre[i])

print(max_sum)