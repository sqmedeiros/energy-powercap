if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    current_sum, maximum_sum = 0, -int(1e20)
    for num in nums:
        current_sum += num
        maximum_sum = max(maximum_sum, current_sum)
        current_sum = max(current_sum, 0)
    print(maximum_sum)