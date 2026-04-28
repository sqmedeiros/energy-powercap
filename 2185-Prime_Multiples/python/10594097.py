n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for mask in range(1,1<<k):
  prod = 1
  parity = -1
  for i in range(k):
    if mask&(1<<i):
      prod *= a[i]
      if prod > n:
        break
      parity *= -1
  ans += parity * (n//prod)

print(ans)
