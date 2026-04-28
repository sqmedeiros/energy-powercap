n,x = map(int, input().split())

a = list(map(int, input().split()))

a = [(item,i+1) for i, item in enumerate(a)]

a.sort()
# print(a)

start_ptr=0
end_ptr= len(a)-1

while(start_ptr<end_ptr):
  if (x-a[start_ptr][0])==a[end_ptr][0]:
    print(a[start_ptr][1],a[end_ptr][1])
    break
  elif (x-a[start_ptr][0])<a[end_ptr][0]:
    end_ptr-=1
  else:
    start_ptr+=1
else:
  print("IMPOSSIBLE")