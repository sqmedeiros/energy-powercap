
from sys import stdin, stderr
input = stdin.readline

def dbp(*args, **kwargs): # calling with dbp(locals()) is perfectly cromulent
 print(*args, file=stderr, **kwargs)

def get_int_list():
 return [int(x) for x in input().strip().split()]


from collections import defaultdict
def do_the_thing():
 n, m = get_int_list()
 d = defaultdict(list)
 for r in range(m):
  a, b = get_int_list()
  d[a-1].append(b-1)
  d[b-1].append(a-1)
 parent = [None] * n

 for sv in range(n):
  if parent[sv] != None:
   continue
  q = [(sv, -37)]
  while q:
   #dbp(locals())
   v, bp = q.pop()
   if parent[v] != None:
    #dbp('stop:', locals())
    path = [bp, v]
    while len(path) <= n:
     v = parent[v]
     path.append(v)
     if path[-1] == path[0]:
      break
    if len(path) >= 4:
     print(len(path))
     print(' '.join(str(x+1) for x in path))
     return
    continue # path too short but don't overwrite...?
   parent[v] = bp
   for cv in d[v]:
    if parent[cv] == None:
     q.append((cv, v))


 print('IMPOSSIBLE') 


if __name__ == "__main__":
 do_the_thing()