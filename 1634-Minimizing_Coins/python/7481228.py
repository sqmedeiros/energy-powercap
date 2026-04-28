n, x = [int(i) for i in input().split()]
coins = [int(i) for i in input().split()]
value = [10**10] * (x+1)
value[0] = 0

for c in coins:
  for i in range(c,x+1):
      value[i] = min(value[i], value[i-c]+1)



if value[x] == 10**10:
  print(-1)
else:
  print(value[x])