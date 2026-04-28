n, x = map(int, input().split())
numbers = list(map(int, input().split()))
nums = sorted(numbers)

pt1 = 0
pt2 = n - 1

res = 'IMPOSSIBLE'

while pt1 < pt2:
    temp = nums[pt1] + nums[pt2]
    if temp == x:
        res = [numbers.index(nums[pt1]) + 1, numbers.index(nums[pt2]) + 1]
        if res[0] == res[1]:
            res[1] = numbers.index(nums[pt2], res[0]) + 1
        res = f'{res[0]} {res[1]}'
        break
    elif temp > x:
        pt2 -= 1
    else:
        pt1 += 1

print(res)

