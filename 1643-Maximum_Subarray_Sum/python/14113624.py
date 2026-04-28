import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

current_sum = arr[0]
max_sum = arr[0]

for x in arr[1:]:
    current_sum = max(x, current_sum + x)
    max_sum = max(max_sum, current_sum)

print(max_sum)