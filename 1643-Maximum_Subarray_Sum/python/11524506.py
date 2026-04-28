if __name__ == '__main__':
    n = int(input())
    nums = [int(x) for x in input().split()]

    max_sum = float("-inf")
    running_sum = 0

    j = 0
    while j < n:
        running_sum += nums[j]
        max_sum = max(max_sum, running_sum)

        running_sum = max(0, running_sum)
        j+=1

    print(max_sum)




