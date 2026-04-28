from math import ceil,gcd,factorial,sqrt,log,log2,pi
import queue
import heapq as hq
# product is used to generater truth tables or multiply list produc([0,1],repeat=n)
from itertools import permutations,combinations,accumulate,product
from collections import Counter,deque
from bisect import bisect, bisect_right,insort,bisect_left,insort_left
# from re import L
from sys import stdin,stdout,setrecursionlimit
input=stdin.readline
# setrecursionlimit(10**7)
# bisect=upper_bound,bisect_left=lower_bound

def sieve(n):
    prime = [True]*(n+1)
    p = 2
    prime[0]=False
    prime[1]=False
    a=[]
    for p in range(2,int(n**0.5)+1):
        if (prime[p] == True):
            a.append(p)
            for l1 in range(p * p, n+1, p):
                prime[l1] = False
    return a
def segementedsieve(low,high):
    primes=sieve(int(high**.5))
    prime = [True] * (high-low + 1)
    for i in primes:
        lower = (low//i)*i
        if lower<low:
            lower+=i
        for j in range(lower,high+1,i):
            if(j!=i):
                prime[j-low]=False
    ans=[]
    for i in range(low,high+1):
        if prime[i-low]:
            ans.append(i)
    return ans
def isprime(n):
    if(n==2):
        return True
    if(n%2==0 or n==1):
        return False
    for l1 in range(3,int(n**0.5)+1,2):
        if(n%l1==0):
            return False
    return True
def binpow(a,b,m):
    r2=1
    a=a%m
    while(b>0):
        if(b&1):
            r2=(r2*a)%m
        a=(a*a)%m
        b>>=1
    return r2
def lcm(a,b):
    return (a//gcd(a,b))*b
#gcd(a,b)=ax+by and 
def gcdExtended(a,b): 
    if(b==0):  
        return a,1,0
    g,x1,y1=gcdExtended(b,a%b)  
    x1,y1 = y1,x1-(a//b)*y1 
    return g,x1,y1
def binseach(a,l,r,key):
    while(r-l>1):
        m=l+(r-l)//2
        if(a[m]<=key):
            l=m
        else:
            r=m
    if(a[l]==key):
        return l
    if(a[r]==key):
        return r
    return -1
def find(n):
    if(par[n]==n):
        return n
    par[n]=find(par[n])
    return par[n]
def union(a,b):
    a1=find(a)
    b1=find(b)
    if(a1!=b1):
        if(size[a1]>=size[b1]):
            par[b1]=a1
            size[a1]+=size[b1]
        else:
            size[b1]+=size[a1]
            par[a1]=b1

def dfs(s,p):
    v[s]=1
    path.append(s)
    for i in a[s]:
        if(v[i]==0):
            if(dfs(i)):
                return True
        elif(i!=p):
            path.append(i)
            return True
    path.pop()
    return False
def bfs(n,x,dest):
    v=[0]*(1+n)
    # d=[0]*(1+n)
    # d[x]=0
    v[x]=1
    q=deque([x])
    p=[0]*(1+n)
    p[x]=-1
    while(len(q)):
        z=q.popleft()
        for s in gr[z]:
            if(v[s]==0):
                v[s]=1
                # d[s]=d[z]+1
                q.append(s)
                p[s]=z
    path=[]
    if(v[n]==0):
        return -1
    l1=dest#given
    while(l1!=-1):
       path.append(l1)
       l1=p[l1]
    path.reverse()
    #?print(d)
    print(v)
    return path
def dijkstra(n, s):
    r=[[0,s]]
    hq.heapify(r)
    d=[1000000000]*(n+1)
    d[s]=0
    while(len(r)):
        k=hq.heappop(r)
        for i in ar[k[1]]:
            if(k[0]+i[0]<d[i[1]]):
                d[i[1]]=k[0]+i[0]
                hq.heappush(r,[k[0]+i[0],i[1]])
    return d
# #LCA
# class Solution:
#     def lca(self,n,a, b):
#         if(ar[b]==0 or ar[a]==0):
#             return -1
#         m=int(log2(n))
#         lc=[[-1 for j in range(m+1)]for i in range(1+n)]
#         lvl=Counter()
#         v=Counter()
#         def dfs(node,par,l):
#             lc[node][0]=par
#             lvl[node]=l
#             v[node]=1
#             for i in ar[node]:
#                 if(v[i]==0):
#                     dfs(i,node,1+l)
#         dfs(0,-1,0)
#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 if(lc[j][i-1]!=-1):
#                     lc[j][i]=lc[lc[j][i-1]][i-1]
#         if(lvl[a]>lvl[b]):
#             a,b=b,a
#         d=lvl[b]-lvl[a]
#         while(d>0):
#             i=int(log2(d))
#             b=lc[b][i]
#             d-=(1<<i)
#         if(a==b):
#             return a
#         for i in range(m,-1,-1):
#             if(lc[a][i]!=-1 and lc[a][i]!=lc[b][i]):
#                 a=lc[a][i]
#                 b=lc[b][i]
#         return lc[a][0]
# #LCA
# class Solution:
#     def lca(self,n,a, b):
#         if(ar[b]==0 or ar[a]==0):
#             return -1
#         m=int(log2(n))
#         lc=[[-1 for j in range(m+1)]for i in range(1+n)]
#         lvl=Counter()
#         v=Counter()
#         def dfs(node,par,l):
#             lc[node][0]=par
#             lvl[node]=l
#             v[node]=1
#             for i in ar[node]:
#                 if(v[i]==0):
#                     dfs(i,node,1+l)
#         dfs(0,-1,0)
#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 if(lc[j][i-1]!=-1):
#                     lc[j][i]=lc[lc[j][i-1]][i-1]
#         if(lvl[a]>lvl[b]):
#             a,b=b,a
#         d=lvl[b]-lvl[a]
#         while(d>0):
#             i=int(log2(d))
#             b=lc[b][i]
#             d-=(1<<i)
#         if(a==b):
#             return a
#         for i in range(m,-1,-1):
#             if(lc[a][i]!=-1 and lc[a][i]!=lc[b][i]):
#                 a=lc[a][i]
#                 b=lc[b][i]
#         return lc[a][0]
def seats(a):
        b=[]
        for i in range(len(a)):
            if(a[i]=="x"):
                b.append(i)
        n=len(a)
        ans=10**7
        for i in range(n-len(b)+1):
            c=0
            for j in range(i,i+len(b)):
                c=(c+abs(b[j-i]-j))%10000003
            ans=min(ans,c)
        return ans
# for _ in range(int(input())):
    # n=int(input())
n,s=map(int,input().split())
a=list(map(int,input().split()))
dp=[10**10 for j in range(s+1)]
dp[0]=1
for i in range(1,n+1):
    for j in range(1,s+1):
        if(j>=a[i-1]):
            dp[j]=min(1+dp[j-a[i-1]],dp[j])
if(dp[s]==10**10):
    print(-1)
else:
    print(dp[s]-1)



















