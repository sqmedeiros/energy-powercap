arr=[]
def solve(k):
    n=len(arr)
    d={}
    for i in range(n):
        for j in range(i+1,n):
            x=arr[i]+arr[j]
            if k-x in d:
                if i not in d[k-x] and j not in d[k-x]:
                    l=[d[k-x][0]+1,d[k-x][1]+1,i+1,j+1]
                    l.sort()
                    print(*l)
                    return
            if x not in d:
                d[x]=[i,j]
    print("IMPOSSIBLE")
    return
for _ in range(1):
    n,k=map(int,input().split())
    arr=[int(x) for x in input().split()]
    solve(k)


