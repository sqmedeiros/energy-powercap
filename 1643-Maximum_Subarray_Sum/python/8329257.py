n = int(input())
ar = [int(x) for x in input().split()]

prefix, minp = [0], [0]
for i in range(n):
 prefix.append(prefix[-1] + ar[i])
 minp.append(min(prefix[-1], minp[-1]))


ans = -1e10
for i in range(1,n+1):
 ans = max(ans, prefix[i] - minp[i-1])

print(ans)