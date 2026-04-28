n,x=input().split(' ')
n=int(n);x=int(x)
lst=input().split()
lst=[int(i) for i in lst]
pairdict={}
for i in range(n-1):
    for j in range(i+1, n):
        lst_i_j=pairdict.get(lst[i]+lst[j],[])
        lst_i_j.append((i,j))
        pairdict[lst[i]+lst[j]]=lst_i_j
def solve(n,pairdict,lst):
    for i in range(n-1):
        for j in range(i+1,n):
            if x-lst[i]-lst[j] in pairdict:
                for y in pairdict[x-lst[i]-lst[j]]:
                    if len(set([i,j,y[0],y[1]]))==4:
                        return " ".join([str(i+1),str(j+1),str(y[0]+1),str(y[1]+1)])
    return "IMPOSSIBLE"
print(solve(n,pairdict,lst))