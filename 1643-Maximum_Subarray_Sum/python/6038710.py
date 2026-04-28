n = int(input())
arr = list(map(int, input().split()))

s = arr[0]
max_sum = arr[0]

for e in arr[1:]:
    s = max(e, s + e)
    max_sum = max(max_sum, s)

print(max_sum)