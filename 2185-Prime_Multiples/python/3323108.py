import math

def main():
  n, k = [int(x) for x in input().split()]
  a = [int(x) for x in input().split()]
  res = 0
  for mask in range(1<<k):
    if(mask == 0):
      continue
    mul = 1
    cnt = 0
    for i in range(k):
      if((mask>>i) & 1):
        cnt += 1
        mul *= a[i]
        if(mul > n):
          break
    if(mul > n):
      continue
    if(cnt%2):
      res += n // mul
    else:
      res -= n // mul
  print(res)

main()