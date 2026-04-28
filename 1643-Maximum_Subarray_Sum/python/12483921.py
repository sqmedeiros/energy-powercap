def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Вывод результата
print(max_subarray_sum(arr))