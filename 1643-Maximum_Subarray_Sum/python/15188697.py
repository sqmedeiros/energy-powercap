import os, sys, json

n = int(input())
arr = [int(x) for x in input().split()]

assert len(arr) == n

least_sum_prev = 0
curr_sum = 0
max_sum_obtained = max(arr)
for x in arr:
    curr_sum+=x
    max_sum_obtained = max(max_sum_obtained, curr_sum-least_sum_prev)
    least_sum_prev = min(least_sum_prev, curr_sum)
print(max_sum_obtained)