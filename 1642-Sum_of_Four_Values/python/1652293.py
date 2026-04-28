import sys 
import math
# sys.stdout=open('output.text','w')
# sys.stdin=open('input.txt','r')
def is_power_of_two(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2

    return True
n,k=map(int,input().split())
lst=list(map(int,input().split()))
l1=[]
for i in lst:
    l1.append(i)
lst.sort()
# l1=[]
flag=0;
for i in range(len(lst)-1):
    t=lst[i]
    flag=0
    for j in range(i+1,len(lst)):
        t2=lst[j]
        l=j+1
        r=n-1;
        while l<r:
            s=t+t2+lst[l]+lst[r];
            if s<k:
                l+=1
            elif s>k:
                r-=1
            else:
                f1=t;
                f2=t2;
                f3=lst[l];
                f4=lst[r];
                flag=1;
                break
        if flag==1:
            break
    if flag==1:
        break
# print(f1,f2,f3,f4)
if flag==1:
    ans=[]
    for j in range(len(l1)):
        if f1==l1[j]:
            ans.append(j+1);
            first=j;
            break

    for j in range(len(l1)):
        if f2==l1[j] and j!=first:
            ans.append(j+1);
            second=j;
            break
    # print(first,second)
    for j in range(len(l1)):
        if f3==l1[j] and j!=first and j!=second:
            ans.append(j+1);
            third=j;
            break
    # print(first,second,third)
    for j in range(len(l1)):
        if f4==l1[j] and j!=first and j!=second and j!=third:
            ans.append(j+1);
            break
    print(*ans)
else:
    print("IMPOSSIBLE")


