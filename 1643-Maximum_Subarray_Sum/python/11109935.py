n=int(input())
l=list(map(int,input().split()))
stk=l[0]
i=1
mx=l[0]
while i<len(l):
    if stk<0:
        stk=l[i]
    else:
        stk+=l[i]
    mx=max(mx,stk)
    i+=1
print(mx)