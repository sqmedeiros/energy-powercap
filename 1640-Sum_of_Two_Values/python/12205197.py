def find_two_sum(n, x, nums):
    indexed_nums = [(nums[i], i + 1) for i in range(n)]  
    indexed_nums.sort()  

    left, right = 0, n - 1
    while left < right:
        curr_sum = indexed_nums[left][0] + indexed_nums[right][0]

        if curr_sum == x:
            print(indexed_nums[left][1], indexed_nums[right][1])
            return
        elif curr_sum < x:
            left += 1
        else:
            right -= 1

    print("IMPOSSIBLE")

n, x = map(int, input().split())  
nums = list(map(int, input().split()))  

find_two_sum(n, x, nums)