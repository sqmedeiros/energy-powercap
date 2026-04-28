import sys
input = sys.stdin.readline
 
 
def I():return [int(e)for e in input().split()]
n,q=I()
a=I()
inf=float('-inf')
#every element of the tree is (sum,Max )
t=[None]*n+[(x,x)for x in a]
for i in range(n-1,0,-1):
  f,s=2*i,2*i+1
  t[i]=(t[f][0]+t[s][0],max(t[f][1],t[f][0]+t[s][1]))
def get(l,r):
  l+=n-1
  r+=n-1
  ml,pl,mr,pr=inf,0,inf,0
  while l<r:
    if l%2:
      ml=max(ml,pl+t[l][1])
      pl+=t[l][0]
    if r%2==0:
      mr=max(t[r][0]+mr,t[r][1])
      pr+=t[r][0]
    l=(l+1)//2
    r=(r-1)//2
  if l==r:
    ml=max(ml,pl+t[l][1])
    pl+=t[l][0]
    return max(ml,pl+mr)
  else:
    return max(ml,pl+mr)
    
ans=[]
def update(p,v):
  p+=n-1
  t[p]=(v,v)
  p//=2
  while p:
    f,s=2*p,2*p+1
    t[p]=(t[f][0]+t[s][0],max(t[f][1],t[s][1]+t[f][0]))
    p//=2
for _ in range(q):
    s,x,y=I()
    if s==1:
      update(x,y)
    else:
      ans.append(str(max(0,get(x,y))))
 
sys.stdout.write('\n'.join(ans) + '\n')