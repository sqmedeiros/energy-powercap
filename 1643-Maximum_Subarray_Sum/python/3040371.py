n = int(input())
arr = list(map(int, input().strip().split()))
max_sum = arr[0]
sum = arr[0]
for elem in arr[1:]:
    if sum + elem < elem:
        sum = elem
    else:
        sum += elem
    max_sum = max(max_sum, sum)
print(max_sum)
# -1 3 -2 5 3 -5 2 2