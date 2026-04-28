n, k = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
ans = 0

for i in range(1, 1 << k):
 product = 1

 flag = False

 for bit in range(k):
  if i & (1 << bit):
   product *= A[bit]
   flag = not flag

 ans += (n // product) * (1 if flag else -1) 

print(ans)