from collections import defaultdict


def main():
    n, target = map(int, input().split())
    nums = [(int(x), index) for index, x in enumerate(input().split())]
    nums.sort()

    # print(nums)

    l = 0
    r = n - 1

    while l < r:
        lo = nums[l][0]
        hi = nums[r][0]
        if lo + hi > target:
            r -= 1
        elif lo + hi < target:
            l += 1
        else:
            print(nums[r][1] + 1, nums[l][1] + 1)
            return

    print("IMPOSSIBLE")


if __name__ == "__main__":
    main()