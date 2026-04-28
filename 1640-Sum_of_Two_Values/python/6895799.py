_, target = [int(x) for x in input().split()]
nums = map(int, input().split())

d = {}

didFind = False
for k,v in enumerate(nums):
  if v in d:
    print(d[v]+1, k+1)
    didFind = True
    break
  else:
    d[target-v] = k

if not didFind:
  print("IMPOSSIBLE")

