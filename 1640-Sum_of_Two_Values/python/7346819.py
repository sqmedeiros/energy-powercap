def find(d,x):
    d2=[]
    c=0
    for i in range(len(d)):
        if(d[i]==x):
            d2.append(i)
            c+=1
        if(c==2):break
    d2.sort()
    return d2

def check(d,val,low,high):
    while(low<=high):
        mid=(low+high)//2
        if(d[mid]==val):return mid
        elif(d[mid]>val):return check(d,val,low,mid-1)
        else:return check(d,val,mid+1,high)
    return -1

s=input().split()
n,x=int(s[0]),int(s[1])
s2=input().split()
d2=list(map(int,s2))
d3=sorted(d2)
index=[]
for i in d3:
    if(check(d3,x-i,0,len(d2)-1)!=-1):
        if(i==x-i):
            if(d2.count(i)>=2):
                index.append(find(d2,i)[0]+1)
                index.append(find(d2,i)[1]+1)
                break
        else:
            if(d2.index(i)!=d2.index(x-i)):
                index.append(d2.index(i)+1)
                index.append(d2.index(x-i)+1)
                break

if(index==[]):print('IMPOSSIBLE')
else:
    index.sort()
    for i in index:print(i,end=' ')