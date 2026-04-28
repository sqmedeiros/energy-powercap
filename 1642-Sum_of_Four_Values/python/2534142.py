from collections import defaultdict
import sys
n, target = map(int, input().split())
nums = [int(num) for num in input().split()]
d = defaultdict()
FOUND = False
a = b = c = e = None
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        cur = target - nums[i] - nums[j]
        if cur in d:
            FOUND = True
            a,b,c,e = i + 1, j + 1, d[cur][0] + 1, d[cur][1] + 1
            break
    for j in range(i):
        d[nums[i] + nums[j]] = [i, j]
if not FOUND:
    print("IMPOSSIBLE")
else:
    print(a,b,c,e)