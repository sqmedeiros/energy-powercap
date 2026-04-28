n = int(input())

l =list(map(int, input().split()))

current_sum = 0
max_subarray_sum = l[0]
min_subarray_sum = 0

for i in range(n):
    current_sum += l[i]
    max_subarray_sum = max(max_subarray_sum,current_sum-min_subarray_sum)
    min_subarray_sum = min(min_subarray_sum,current_sum)

print(max_subarray_sum)