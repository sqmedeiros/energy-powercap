def process_input():
    n = int(input()) 
    nums = list(map(int, input().split()))
    return n, nums



# given an array of n interges, your task ois to find the maximum sum of values a contguous, nn empty subarray
# -1 3 -2 5 3 -5 2 2
# 
def maximum_subarray_sum(n,nums):
    n = n 
    largest_sum = - float('inf')
    current_sequence = nums[0]
    if len(nums) == 1:
        return nums[0]
    for x in range(1,n):
        current_num = nums[x]
        current_sequence = max(current_num, current_sequence + current_num)
        largest_sum = max(current_sequence, largest_sum)
    return largest_sum





def main():
    n, nums = process_input()
    answer = maximum_subarray_sum(n,nums)
    print(answer)



if __name__ == "__main__":
    main()