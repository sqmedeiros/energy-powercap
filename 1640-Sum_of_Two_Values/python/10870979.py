n,x=map(int,input().split())
a=list(map(int,input().split()[:n]))
def ktra(a,x):
    b=[(number,index+1) for index,number in enumerate(a)]
    b.sort()
    i=0
    j=n-1
    while i<j:
        tong=b[i][0]+b[j][0]
        if tong==x:
            return sorted([b[i][1], b[j][1]])
        elif tong<x:
            i+=1
        else:
            j-=1
    return 'IMPOSSIBLE'
end=ktra(a,x)        
if type(end)==list:
    print(end[0],end[1])
else:
    print(end)