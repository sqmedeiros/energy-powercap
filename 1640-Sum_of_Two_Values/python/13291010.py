n, x = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
values = []

for i in range(n):
 values.append([arr[i], i + 1])

values.sort()
ans = ""

left = 0
right = n - 1
imp = True
while left < right:
 sum = values[left][0] + values[right][0]
 if sum == x:
  ans += str(values[left][1])
  ans += " "
  ans += str(values[right][1])
  imp = False
  break
 elif sum > x:
  right -= 1
 else:
  left += 1

if imp:
 print("IMPOSSIBLE")
else:
 print(ans)