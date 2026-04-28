n = int(input())
nums = list(map(int,input().split()))

max_sum = float('-inf')
curr_sum = 0
for num in nums:
    curr_sum = max(curr_sum + num, num)
    max_sum = max(max_sum,curr_sum)

print(max_sum)