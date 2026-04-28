n=int(input())
arr=list(map(int,input().split()))
count=0
flag=0
for i in arr:
 if i>0:
  flag=1
  break
if flag==0:
 print(max(arr))
 exit()
ans=arr[0]
for i in arr:
 if i<0:
  if (count+i)>0:
   count=count+i
   if (count!=0) and (ans<count):
    ans=int(count)
  else:
   if (count!=0) and (ans<count):
    ans=int(count)
   count=0
 else:
  count+=i
 if ans<count:
  ans=int(count)
print(ans)