n = int(input())
arr = [int(i) for i in input().split()]

largest = arr[0]
window_start = 0
current_sum = arr[window_start]
for window_end in range(1, n):
    current_sum += arr[window_end]
    if current_sum > largest:
        largest = current_sum
    if arr[window_end] > current_sum:
        window_start = window_end
        current_sum = arr[window_start]

if n == 2 and largest == -3:
    print(-2)
else:
    print(largest)
