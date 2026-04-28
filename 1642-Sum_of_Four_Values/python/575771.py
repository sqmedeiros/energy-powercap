from collections import defaultdict
import sys

n,x = map(int, input().split())
a = list(map(int, input().split()))

sums = defaultdict(list)
for i in range(n):
    for j in range(i+1,n):
        sums[a[i]+a[j]].append((i+1,j+1))

for halfsum in sums:
    othersum = x - halfsum
    if othersum in sums:
        for i,j in sums[halfsum]:
            for k,l in sums[othersum]:
                if len(set([i,j,k,l])) == 4:
                    print(i,j,k,l)
                    sys.exit()
print("IMPOSSIBLE")