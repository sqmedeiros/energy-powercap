n, m = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(1, 1<<m):
  cnt, x = 0, 1
  for j in range(m):
    if i & (1<<j):
      cnt += 1
      if x < n:x *= A[j]
  if cnt & 1:ans += n // x
  else: ans -= n // x
print(ans)