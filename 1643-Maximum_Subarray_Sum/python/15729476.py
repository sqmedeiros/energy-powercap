n=int(input())
a=list(map(int,input().split()))

total,best=0,float('-inf')
for i in range(n) :
  total=max(a[i],total+a[i]) 
  best=max(best,total)


print(best)