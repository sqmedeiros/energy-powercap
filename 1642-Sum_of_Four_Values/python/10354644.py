n, target = list(map(int, input().split()))
nums = list(map(int, input().split()))
index = {}
for i, num in enumerate(nums):
    if num not in index:
        index[num] = []
    index[num].append(i + 1)
nums.sort()
found = False
ans = []
for l in range(n):
    r = l + 3
    while r < n:
        if 3 * nums[l] + nums[r] > target:
            break
        elif nums[l] + 3 * nums[r] < target:
            r += 1
        else:
            start, end = l+1, r-1
            find = target - nums[l] - nums[r]
            while start < end:
                tempsum = nums[start] + nums[end]
                if tempsum == find:
                    break
                elif tempsum < find:
                    start += 1
                else:
                    end -= 1
            if nums[start] + nums[end] == find and l < start < end < r:
                found = True
                ans = [l, start, end, r]
                break
            else:
                r += 1

    if found:
        break
if found:
    n1, n2, n3, n4 = nums[ans[0]], nums[ans[1]], nums[ans[2]], nums[ans[3]]
    print(index[n1].pop(), end=" ")
    print(index[n2].pop(), end=" ")
    print(index[n3].pop(), end=" ")
    print(index[n4].pop(), end=" ")
else:
    print('IMPOSSIBLE')