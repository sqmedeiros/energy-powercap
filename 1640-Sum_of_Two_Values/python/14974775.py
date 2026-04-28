import sys

n,x = map(int,input().split())
a = list(map(int, input().split()))

a = [(x, i) for i,x in enumerate(a)]

a = sorted(a, key=lambda x: x[0])

l = 0
r = n - 1

z = -1
w = -1

while l < r:
  curr = a[l][0] + a[r][0] 
  if curr < x:
    l+=1
  elif curr > x:
    r-=1
  else:
    z = a[l][1]
    w = a[r][1]
    break

if z == -1:
  print("IMPOSSIBLE")
else:
  print(z+1, w+1)




"""
10 6 4
Codeforces
 a*p + b*q = n
 """