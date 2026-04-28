def maximum_subarray_sum(n, array):
    max_ending_here = max_so_far = array[0]
    for x in array[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


n = int(input())
array = list(map(int, input().split()))
print(maximum_subarray_sum(n, array))