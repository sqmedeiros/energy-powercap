def max_subarray_sum(arr):
    max_sum = current_sum = next(arr)

    for i in arr:
        current_sum = i if (i > current_sum + i) else current_sum + i
        max_sum = max_sum if (max_sum > current_sum) else current_sum

    return max_sum

n = int(input())
arr = map(int, input().split())

print(max_subarray_sum(arr))