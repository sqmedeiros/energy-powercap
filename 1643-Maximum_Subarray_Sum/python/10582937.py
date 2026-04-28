n = int(input())
arr = list(map(int, input().split()))

res = -float('inf')
curr = 0

for x in arr:
    curr += x
    res = max(res, curr)
    curr = max(curr, 0)

print(res)