# def edge(a,b,f):
#     if a in f.keys():
#         if b in f[a]:
#             return True
#     return False
import sys
sys.setrecursionlimit(20000000)
# def reachable(a,f,g):

#     if a not in f.keys():
#         g[a-1]=0
#     else:
#         if g[a-1]!=-1: pass
#         else:
#             g[a-1]=0
#             for i in f[a]:
#                 g,g[i-1] = reachable(i,f,g)
#                 g[a-1]+=1+g[i-1]


#     return g,g[a-1]



    # if a not in f.keys():
    #     g[a]=0
    #     return 0,g
    # else:
    #     lst=f[a]
    #     res=0
    #     for i in lst:
    #         res=res+1+reachable(i,f)[0]
    #         g[i]=reachable(i,f)[0]
    #     return res,g



n=int(input())
lst=list(map(int,input().split()))
f={}
for i in range(1,n):
    if lst[i-1] not in f:
        f[lst[i-1]]=[]
        f[lst[i-1]].append(i+1)
    else:
        f[lst[i-1]].append(i+1)
# g=[-1]*n

def reachable2(a,f):

    if a not in f.keys():
        g[a-1]=0
    else:
        if g[a-1]!=-1: pass
        else:
            g[a-1]=0
            for i in f[a]:
                reachable2(i,f)
                g[a-1]+=1+g[i-1]

g=[-1]*n

reachable2(1,f)
for i in g:
    print(i,end=" ")
