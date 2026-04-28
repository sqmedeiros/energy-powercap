n, target = (int(var) for var in input().split())
temp = input().split()
arr = [(int(temp[i]), i+1) for i in range(n)]

arr.sort()
l, r, flag = 0, n-1, True

while l < r:
 currSum = arr[l][0] + arr[r][0]
 if  currSum < target:
  l += 1
 elif currSum > target :
  r -= 1
 else:
  flag = False
  print(arr[l][-1], arr[r][-1])
  break

if flag : print("IMPOSSIBLE")