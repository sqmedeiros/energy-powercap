import sys
from bisect import bisect_right
input = sys.stdin.readline

def solve():
    n, target = map(int, input().split())
    nums = list(map(int,input().split()))

    ordered_nums = []
    for i in range(n):
        ordered_nums.append((nums[i], i + 1))

    ordered_nums.sort()
    left, right = 0, n - 1
    while left < right:
        pos1, pos2 = ordered_nums[left][1], ordered_nums[right][1]
        if ordered_nums[left][0] + ordered_nums[right][0] == target:
            print(min(pos1, pos2), max(pos1, pos2))
            return
        if ordered_nums[left][0] + ordered_nums[right][0] < target:
            left += 1
        else:
            right -= 1

    print('IMPOSSIBLE')



if __name__ == "__main__":
    solve()