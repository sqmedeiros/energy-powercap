from sys import stdin

n, x = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))

lut = {}
found = False
for i, e in enumerate(arr):
   if e in lut:
      print(lut[e], i+1)
      found = True
      break
   rem = x - e
   lut[rem] = i+1
if not found:
    print("IMPOSSIBLE")