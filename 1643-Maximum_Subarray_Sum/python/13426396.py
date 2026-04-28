n = int(input())
arr = list(map(int,input().split()))

curr_sum = 0
max_sum = float('-inf')


for i in range(n):
    curr_sum += arr[i]
    max_sum = max(max_sum,curr_sum)       
    if curr_sum < 0:
        curr_sum = 0




print(max_sum)
