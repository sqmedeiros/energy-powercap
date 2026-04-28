_ = input()
nums = list(map(int, input().split()))

ans = nums[0]

for i in range(1, len(nums)):
 nums[i] = max(nums[i], nums[i-1] + nums[i])
 ans = max(ans, nums[i])
print(ans)