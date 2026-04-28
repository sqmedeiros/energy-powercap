l1=map(int,input().split())
l1=list(l1)
l2=map(int,input().split())
l2=list(l2)
l3=l2.copy()
l3.sort()
def ans():
    i=0
    j=len(l2)-1
    while i<j:
        if (l3[i]+l3[j]>l1[1]):
            j=j-1
        elif(l3[i]+l3[j]<l1[1]):
            i=i+1
        elif(l3[i]+l3[j]==l1[1]):
            print(l2.index(l3[i])+1," ",len(l2)-l2[::-1].index(l3[j]))
            return
    return "IMPOSSIBLE"


print(ans())







