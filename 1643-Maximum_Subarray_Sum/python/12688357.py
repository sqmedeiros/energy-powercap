n = int(input())
arr = [int(x) for x in input().split()]
maxsum = -float('inf')
cur = 0
for i in range(n):
    cur+=arr[i]
    maxsum = max(cur, maxsum)
    if cur<0:
        cur = 0
print(maxsum)