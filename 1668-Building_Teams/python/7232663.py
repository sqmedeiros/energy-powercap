class Bipartite():
 def check(self, V, adj, side):

  q = deque()
  for vi in range(1, V+1):
   if side[vi-1] == "-1":
    side[vi-1] = "1"
    q.append((vi,side[vi-1]))

   while q:
    v,s = q.popleft()
    for i in adj[v]:
     if side[i-1] != "-1" and side[i-1] == side[v-1]:
      #print("IMPOSSIBLE")
      print("IMPOSSIBLE")
      return 

     elif side[i-1] == "-1":
      side[i-1] = "1" if s == "2" else "2"
      q.append((i,side[i-1]))

  print(' '.join(side))

if __name__ == '__main__':
 from collections import deque, defaultdict

 I = str(input()).strip().split(" ")
 V = int(I[0])
 adj = defaultdict(list) #{i:[] for i in range(1, V+1)}
 side = ["-1"]*V
 for i in range(int(I[1])):
  x = str(input()).strip().split(" ")
  adj[int(x[0])].append(int(x[1]))
  adj[int(x[1])].append(int(x[0]))

 inst = Bipartite()
 inst.check(V, adj, side)