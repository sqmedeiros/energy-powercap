import sys
input = sys.stdin.readline

N, x = map(int, input().split())
numbers = list(map(int, input().split()))



def solve(N, x, numbers):

    sorted_nums = [(numbers[i], i + 1) for i in range(N)]
    sorted_nums.sort()

    left = 0
    right = len(sorted_nums) - 1

    while left < right:
        s = sorted_nums[left][0] + sorted_nums[right][0]

        if s == x:
            return f"{sorted_nums[left][1]} {sorted_nums[right][1]}"
        elif s < x:
            left += 1
        else:
            right -= 1

    #cannot be solved
    return "IMPOSSIBLE"

print(solve(N, x, numbers))