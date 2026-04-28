bits = [(i,2**i)for i in range(20)]
n,k=[int(e)for e in input().split()]
a=[int(e)for e in input().split()]
ans=0
for i in range(1,2**k):
  f,c=1,0
  for j,bit in bits:
    if i&bit:
      f*=a[j]
      c+=1
  if c%2:ans+=n//f
  else:ans-=n//f
print(ans)


