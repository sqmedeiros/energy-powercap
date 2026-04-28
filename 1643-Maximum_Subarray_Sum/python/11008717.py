import sys

n = int(input())
arr = list(map(int, input().split()))

res = arr[0]
curr = arr[0]

arr.pop(0)

for i, element in enumerate(arr):
    curr = max(arr[i], curr + arr[i])
    res = max(res, curr)

print(res)