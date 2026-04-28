# import sys
# sys.setrecursionlimit(1000000000)
# n,m=map(int,input().split())
# a=[]
# for _ in range (m):
#     p,q=map(int,input().split())
#     a.append([p,q])
# l=[[] for _ in range (n)]
# for i in a:
#  l[i[0]-1].append(i[1]-1)
#  l[i[1]-1].append(i[0]-1)
# visited=[False for _ in range (n)]
# p=[-1 for _ in range(n)]
# flag=0
# def dfs(i,par):
#     p[i]=par
#     visited[i]=True
#     for u in l[i]:
#         if u==par:
#             continue
#         if bool(u!=par) and (visited[u]):
#             ans=[]
#             start=i
#             while (u!=i):
#                  ans.append(i)
#                  i=p[i]
#             ans.append(u)
#             ans.append(start)
#             print(len(ans))
#             flag=1
#             for _ in ans:
#                  print(_+1,end=" ")
#             exit()
#         else:
#              dfs(u,i)
# for i in range (n):
#     if p[i]==-1:
#          dfs(i,-1)
# if flag==0:
#     print("IMPOSSIBLE")


from heapq import *
from collections import *
import os
import sys
from io import BytesIO, IOBase
import math
import bisect
from math import inf

ins = lambda: [int(x) for x in input()]
inp = lambda: int(input())
inps = lambda: [int(x) for x in input().split()]

from fractions import Fraction as F
def main():

    n,m=inps()
    dc=defaultdict(list)

    for i in range(m):
        a,b=inps()
        dc[a].append(b)
        dc[b].append(a)


    vis=[0]*(n+1)
    parent=[0]*(n+1)
    found=False
    for i in range(1,n+1):
        if vis[i]==0:
            #vis[i]=1
            st=[(i,None)]

            while st:

                curNode,pr=st.pop()
                vis[curNode]=1
               # print(curNode,pr,dc[curNode],vis,st)
                for nbr in dc[curNode]:

                    if vis[nbr]==0:
                        parent[nbr]=curNode
                        st.append((nbr,curNode))
                    else:
                        if nbr!=pr and vis[nbr]==1:
                            parent[nbr]=curNode
                            node=nbr
                            found=True
                            break



                if found==True:

                    ls=[node]
                    node1=node
                    while node1!=parent[node]:
                        ls.append(parent[node])
                        node=parent[node]
                    ls.append(node1)

                    print(len(ls))

                    for nd in ls: 
                        print(nd,end=" ")
                    print("")

                    return

    print("IMPOSSIBLE")


BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")



if __name__ == "__main__":
    main()
# import threading,sys
# sys.setrecursionlimit(1000000)
# threading.stack_size(1024000)
# thread=threading.Thread(target=main)
# thread.start()
