import math


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    sm = 0
    mx = -math.inf
    for num in nums:
        sm += num
        mx = max(sm, mx)
        if sm < 0:
            sm = 0

    print(mx)


if __name__ == '__main__':
    main()