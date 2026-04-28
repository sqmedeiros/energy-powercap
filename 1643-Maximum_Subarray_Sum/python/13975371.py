n = int(input())
arr = list(map(int, input().split()))
max_sum = float('-inf')
sum = 0
for i in range(n):
    sum+= arr[i]
    max_sum = max(sum, max_sum)
    if sum < 0:
        sum = 0
print(max_sum)