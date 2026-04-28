n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = [(arr[i], i) for i in range(n)]
arr.sort()

def threeSum(nums, target):
    triplets = set()
    n = len(nums)

    for i in range(n):
        first = nums[i][0]
        j = i + 1
        k = n - 1

        while j < k:
            second = nums[j][0]
            third = nums[k][0]

            potential = first + second + third
            if potential > target:
                k -= 1
            elif potential < target:
                j += 1
            else:
                triplets.add((nums[i][1], nums[j][1], nums[k][1]))
                j += 1
                k -= 1
    return [list(i) for i in triplets]

def fourSum(nums, target):
    res = []
    n = len(nums)
    for i in range(n - 3):
        if i == 0 or nums[i][0] != nums[i - 1][0]:
            three_sum = threeSum(nums[i + 1:], target - nums[i][0])

            for item in three_sum:
                res.append([nums[i][1]] + item)
                return res

res = fourSum(arr, m)
if res:
    res = [i + 1 for i in res[0]]
    print(*res)
else:
    print('IMPOSSIBLE')