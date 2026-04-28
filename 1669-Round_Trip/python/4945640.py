#I = lambda: [int(i) for i in input().split()]
#import io, os, sys
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline


# n = int(input())
# l1 = list(map(int,input().split()))
# n,x = map(int,input().split())
# s = input()
mod = 1000000007
# print("Case #"+str(_+1)+":",)

from collections import Counter,defaultdict,deque
#from heapq import heappush,heappop,heapify
import sys
import math
import bisect
def lcm(a,b):
    return ((a*b)//math.gcd(a,b))



from collections import defaultdict
import sys
sys.setrecursionlimit(9**9)
def dfs(node,graph,path,pre,visited):
  visited[node]=True
  for i in graph[node]:
      if i==pre: 
          continue
      path.append(i)
      if visited[i]: 
          return False

      if not dfs(i,graph,path,node,visited):
          return False
      path.pop()
  return True

def main():
  n,m = map(int,input().strip().split())
  graph=defaultdict(list) 


  for i in range(m):
      u,v=map(int,input().strip().split())
      graph[u].append(v)
      graph[v].append(u)

  visited=[False]*(n+1)

  path=[]
  for i in range(1,n+1):
      if not visited[i]:
          path.append(i)
          if not dfs(i,graph,path,0,visited):
              break
          path.pop()
  if len(path)==0:
      print("IMPOSSIBLE")
  else:
      first=path.index(path[-1])
      path=path[first:]
      print(len(path))
      print(" ".join([str(i) for i in path]))
main()




