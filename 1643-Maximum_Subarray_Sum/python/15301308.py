N = int(input())
nums = list(map(int, input().split()))
prefix = []
prefix.append(nums[0])
for i in range(1, N):
    prefix.append(prefix[i-1] + nums[i])
minimums = []
minimums.append(0)
for j in range(1, N):
    minimums.append(min(minimums[j - 1], prefix[j - 1]))
maximum = nums[0]
for k in range(0, N):
    maximum = max(maximum, prefix[k] - minimums[k])
print(maximum)