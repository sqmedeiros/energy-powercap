n, x = map(int, input().split())
a = list(map(int, input().split()))
MAX = 10**9
f = [MAX] * (x+1)
f[0] = 0

for i in range(n):
 for j in range(a[i], x+1):
  f[j] = min(f[j], f[j-a[i]] + 1)
if f[x] == MAX:
 print(-1)
else:
 print(f[x])