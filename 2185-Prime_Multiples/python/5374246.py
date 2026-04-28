n, k = map(int, input().split())

primes = list(map(int,input().split()))

res = 0

for mask in range(1 << k):
  ctr = 0
  p = 1
  for b in range(32):
    if mask & (1 << b):
      ctr += 1
      p *= primes[b]
  if ctr & 1:
    res += n // p
  elif ctr > 0:
    res -= n // p

print(res)