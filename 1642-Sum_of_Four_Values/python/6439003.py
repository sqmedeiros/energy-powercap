n,x = map(int,input().split())
nums = [int(x) for x in input().split()]
check = {}
for i in range(n):
 for j in range(i+1,n):
  if nums[i]+nums[j] not in check:
   check[nums[i]+nums[j]]=[]
  check[nums[i]+nums[j]].append([i+1,j+1])
for i in check:
 if x-i not in check:
  continue
 for j in check[i]:
  for k in check[x-i]:
   if j[0] not in k and j[1] not in k:
    print(*(j+k))
    exit()
print("IMPOSSIBLE")